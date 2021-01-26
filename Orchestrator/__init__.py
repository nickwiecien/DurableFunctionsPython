import logging
import json

import azure.functions as func
import azure.durable_functions as df

from datetime import datetime
from itertools import chain

from helper import GetSalesDataInput, GetSalesDataInput, ProcessDataInput


def orchestrator_function(context: df.DurableOrchestrationContext):

    regions_and_divisions = yield context.call_activity('GetRegionsAndDivisions')

    get_data_tasks = []
    for region in regions_and_divisions['regions']:
        for division in regions_and_divisions['divisions']:
            input = GetSalesDataInput(division, region)
            get_data_tasks.append(context.call_activity('GetSalesData', input.to_json()))
    get_data_results = yield context.task_all(get_data_tasks)

    sales_data = [json.loads(x) for x in get_data_results if x is not None]
    sales_data = list(chain.from_iterable(sales_data))
    sales_data = [json.loads(x) for x in sales_data]

    #Debugging
    sales_data = sales_data[0:10]

    process_data_tasks = []

    time = datetime.now()
    run_id = time.strftime("%m%d%Y-%H%M%S")

    for customer in sales_data:
        process_data_input = ProcessDataInput(customer['region'], customer['division'], customer['customerId'], run_id, customer['monthlySalesTotal'])
        process_data_tasks.append(context.call_activity("ProcessData", process_data_input.to_json()))
    
    process_data_results = yield context.task_all(process_data_tasks)

    yield context.call_activity('SaveData', json.loads(process_data_results[0])['partitionKey'])
   

main = df.Orchestrator.create(orchestrator_function)