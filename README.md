# DurableFunctionsPython

This project was adapted from [DurableFunctionsDemo](https://github.com/13daysaweek/DurableFunctionsDemo) developed by Chris House - Microsoft Cloud Solution Architect. For details about function architecture, please visit the linked repository.

## Environment Setup
Before running this project, create a `local.settings.json` file in the project directory.  This file needs to have the following entries under the `values` section:
  
| Key                                 | Value                                    |
|-------------------------------------|------------------------------------------|
| AzureWebJobsStorage                 | The connection string to the storage account used by the Functions runtime.  To use the storage emulator, set the value to UseDevelopmentStorage=true |
| FUNCTIONS_WORKER_RUNTIME            | Set this value to `python` as this is a python Function App |
| AZURE_SQL_CONNECTION_STRING | A SQL connection string pointing to an Azure SQL DB. See [DurableFunctionsDemo](https://github.com/13daysaweek/DurableFunctionsDemo) for details on database creation |
| STORAGE_ACCOUNT_CONNECTION     | Connection string to a storage account that will be used by the Function to read the input blob containing regions and divisions |
| STORAGE_ACCOUNT_NAME     | Name of a storage account that will be used to store processed data |
| STORAGE_ACCOUNT_KEY     | Key to the storage account that will be used to store processed data |
| STORAGE_ACCOUNT_TABLE     | Name of the storage account table where processed data will be stored |