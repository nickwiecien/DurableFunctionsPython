import logging
from helper import GetSalesDataInput, SalesDataItem, GetSalesDataOutput
import json
import pyodbc
import os

def main(input: GetSalesDataInput) -> str:

    materialized_data = []

    #Establish connection to backend database, query sales data by region/division pair
    connection_string = os.environ.get('AZURE_SQL_CONNECTION_STRING')
    with pyodbc.connect(connection_string) as conn:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM SalesData WHERE Region='{}' AND Division='{}'".format(input.region, input.division)
            cursor.execute(sql)
            row = cursor.fetchone()
            while row:
                new_sales_data_item = SalesDataItem(row[0], row[1], row[2], row[3], row[4], row[5])
                materialized_data.append(new_sales_data_item)
                row = cursor.fetchone()

    output = []
    
    if len(materialized_data)>0:
        #Gather list of unique customers (for the target division/region)
        customer_ids = list(set([x.customerId for x in materialized_data]))
        #Calculate total monthly sales for each customer
        for id in customer_ids:
            filtered = [x for x in materialized_data if x.customerId==id]
            first = filtered[0]
            monthly_sales_total = float(sum(x.transactionAmount for x in filtered))
            output.append(GetSalesDataOutput(first.region, first.division, first.customerId, monthly_sales_total))

    return output
