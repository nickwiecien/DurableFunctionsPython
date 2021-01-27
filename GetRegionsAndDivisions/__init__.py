import logging
import tempfile
import json
import azure.functions as func

async def main(input: str, inputBlob: func.InputStream) -> func.InputStream:
    regions_and_divisions = json.loads(inputBlob.read())
    return regions_and_divisions

