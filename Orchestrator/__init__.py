import logging
import json

import azure.functions as func
import azure.durable_functions as df

from datetime import datetime
from itertools import chain

from helper import GetSalesDataInput, GetSalesDataOutput, ProcessDataInput


def orchestrator_function(context: df.DurableOrchestrationContext):

    #Retrieve a list of regions and divisions
    regions_and_divisions = yield context.call_activity('GetRegionsAndDivisions')

    #For each region/division pair, query database for sales results
    get_data_tasks = []
    for region in regions_and_divisions['regions']:
        for division in regions_and_divisions['divisions']:
            get_data_tasks.append(context.call_activity('GetSalesData', GetSalesDataInput(division, region)))
    get_data_results = yield context.task_all(get_data_tasks)

    #Filter sales data results to non-null entries, and flatten 2D array
    sales_data = [x for x in get_data_results if x is not None]
    sales_data = list(chain.from_iterable(sales_data))

    process_data_tasks = []

    #Create run id (timestamp) to be used as a partition key when adding data to Azure table storage
    run_id = datetime.now().strftime("%m%d%Y-%H%M%S")

    #Process all sales data results (i.e., ML + anomaly prediction)
    for customer in sales_data:
        process_data_input = ProcessDataInput(customer.region, customer.division, customer.customerId, run_id, customer.monthlySalesTotal)
        process_data_tasks.append(context.call_activity("ProcessData", process_data_input))
    
    process_data_results = yield context.task_all(process_data_tasks)

    #Save all processed results to database
    yield context.call_activity('SaveData', process_data_results[0].partitionKey)
   

main = df.Orchestrator.create(orchestrator_function)