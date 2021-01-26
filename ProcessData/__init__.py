import logging
import time
import random
import json
import azure.functions as func
from helper import ProcessDataInput, ProcessDataResult

def main(input: ProcessDataInput, table: func.Out[str]) -> str:

    time.sleep(1)

    random_result = random.random()
    row_key = '{}-{}-{}'.format(input.region, input.division, input.customerId)

    process_data_result = ProcessDataResult(input.region, input.division, 
        input.customerId, random_result, row_key, input.runId)
        
    table.set(ProcessDataResult.to_json(process_data_result))

    return process_data_result
    
