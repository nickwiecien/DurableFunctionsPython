import logging
import time
import random
import json
import azure.functions as func
from helper import ProcessDataInput, ProcessDataResult

async def main(input: ProcessDataInput, table: func.Out[str]) -> str:

    #Simulating ML magic
    time.sleep(1)

    #Random number used in lieu of a true anomaly prediction; this should be a model prediction
    random_result = random.random()

    #Generate a unique row key for each prediction
    row_key = '{}-{}-{}'.format(input.region, input.division, input.customerId)

    process_data_result = ProcessDataResult(input.region, input.division, 
        input.customerId, random_result, row_key, input.runId)

    #Push result to Azure Table defined in input bindings        
    table.set(ProcessDataResult.to_json(process_data_result))

    return process_data_result
    
