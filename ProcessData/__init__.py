import logging
import time
import random
import json
import azure.functions as func
from helper import ProcessDataInput, ProcessDataResult

def main(input: str, table: func.Out[str]) -> str:
    input_json = json.loads(input)
    process_data_input = ProcessDataInput(input_json['region'], input_json['division'], input_json['customerId'], input_json['runId'], input_json['monthlySalesTotal'])
    time.sleep(1)

    random_result = random.random()
    row_key = '{}-{}-{}'.format(process_data_input.region, process_data_input.division, process_data_input.customerId)

    process_data_result = ProcessDataResult(process_data_input.region, process_data_input.division, 
        process_data_input.customerId, random_result, row_key, process_data_input.runId)
        
    table.set(process_data_result.to_json())

    return process_data_result.to_json()
    
