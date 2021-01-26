import logging
import json
import os

import azure.functions as func
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import pandas as pd
import tempfile

def main(runId: str, table) -> str:

    table_service = TableService(account_name=os.environ.get('STORAGE_ACCOUNT_NAME'), account_key=os.environ.get('STORAGE_ACCOUNT_KEY'))
    
    rows = table_service.query_entities(os.environ.get('STORAGE_ACCOUNT_TABLE'), filter="PartitionKey eq '{}'".format(runId))
    my_rows = []
    for row in rows:
        my_rows.append(row)
    df = pd.DataFrame(my_rows)
    print(df)
    
    return f"Hello {runId}!"
