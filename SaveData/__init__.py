import logging
import json
import os

import azure.functions as func
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import pandas as pd
import tempfile
import pyodbc

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def main(runId: str, table) -> str:

    table_service = TableService(account_name=os.environ.get('STORAGE_ACCOUNT_NAME'), account_key=os.environ.get('STORAGE_ACCOUNT_KEY'))
    
    rows = table_service.query_entities(os.environ.get('STORAGE_ACCOUNT_TABLE'), filter="PartitionKey eq '{}'".format(runId))

    tuples = []
    for row in rows:
        tuples.append((row['PartitionKey'], row['region'], row['division'], row['customerId'], row['salesAnomalyCalculation']))

    #insert tuples into db - https://stackoverflow.com/questions/5693885/pyodbc-very-slow-bulk-insert-speed
    connection_string = os.environ.get('AZURE_SQL_CONNECTION_STRING')
    with pyodbc.connect(connection_string) as conn:
        with conn.cursor() as cursor:
            cursor.fast_executemany= True
            stmt = "INSERT INTO SalesAnomalyResults (RunIdentifier, Region, Division, CustomerId, AnomalyCalculationResult) VALUES (?, ?, ?, ?, ?)"
            for chunk in chunks(tuples, 5000):
                cursor.executemany(stmt, chunk)
                cursor.commit()


    return f"{runId}"
