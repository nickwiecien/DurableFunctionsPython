#Serializable class definition reference:
#https://github.com/Azure/azure-functions-durable-python/tree/dev/samples/serialize_arguments

import json
import typing

class GetSalesDataInput(object):
  def __init__(self, division, region):
    self.division = division
    self.region = region

  @staticmethod
  def to_json(obj: object) -> str:
    return json.dumps(obj.__dict__)
 
  @staticmethod
  def from_json(json_str: str) -> object:
      inputs = json.loads(json_str)
      obj = GetSalesDataInput(inputs['division'], inputs['region'])
      return obj

class GetSalesDataOutput(object):
    def __init__(self, region, division, customerId, monthlySalesTotal):
        self.region = region
        self.division = division
        self.customerId = customerId
        self.monthlySalesTotal = monthlySalesTotal

    @staticmethod
    def to_json(obj: object) -> str:
        return json.dumps(obj.__dict__)

    @staticmethod
    def from_json(json_str: str) -> object:
        inputs = json.loads(json_str)
        obj = GetSalesDataOutput(inputs['region'], inputs['division'], inputs['customerId'], inputs['monthlySalesTotal'])
        return obj

class ProcessDataInput(object):
    def __init__(self, region, division, customerId, runId, monthlySalesTotal):
        self.region = region
        self.division = division
        self.customerId = customerId
        self.runId = runId
        self.monthlySalesTotal = monthlySalesTotal
    
    @staticmethod
    def to_json(obj: object) -> str:
        return json.dumps(obj.__dict__)

    @staticmethod
    def from_json(json_str: str) -> object:
        inputs = json.loads(json_str)
        obj = ProcessDataInput(inputs['region'], inputs['division'], inputs['customerId'], inputs['runId'], inputs['monthlySalesTotal'])
        return obj

class ProcessDataResult(object):
    def __init__(self, region, division, customerId, salesAnomalyCalculation, rowKey, partitionKey):
        self.region = region
        self.division = division
        self.customerId = customerId
        self.salesAnomalyCalculation = salesAnomalyCalculation
        self.rowKey = rowKey
        self.partitionKey = partitionKey

    @staticmethod
    def to_json(obj: object) -> str:
        return json.dumps(obj.__dict__)

    @staticmethod
    def from_json(json_str: str) -> object:
        inputs = json.loads(json_str)
        obj = ProcessDataResult(inputs['region'], inputs['division'], inputs['customerId'], inputs['salesAnomalyCalculation'], inputs['rowKey'], inputs['partitionKey'])
        return obj

class SalesAggregateInput(object):
    def __init__(self, regions, divisions):
        self.regions = regions
        self.divisions = divisions

    @staticmethod
    def to_json(obj: object) -> str:
        return json.dumps(obj.__dict__)

    @staticmethod
    def from_json(json_str: str) -> object:
        inputs = json.loads(json_str)
        obj = SalesAggregateInput(inputs['regions'], inputs['divisions'])
        return obj
        
class SalesAnomaly(object):
    def __init__(self, salesAnomalyId, runId, region, division, customerId, anomalyCalculationResult):
        self.salesAnomalyId = salesAnomalyId
        self.runId = runId
        self.region = region
        self.division = division
        self.customerId = customerId
        self.anomalyCalculationResult = anomalyCalculationResult

    @staticmethod
    def to_json(obj: object) -> str:
        return json.dumps(obj.__dict__)

    @staticmethod
    def from_json(json_str: str) -> object:
        inputs = json.loads(json_str)
        obj = SalesAnomaly(inputs['salesAnomalyId'], inputs['runId'], inputs['region'], inputs['division'], inputs['customerId'], inputs['anomalyCalculationResult'])
        return obj

class SalesDataItem(object):
    def __init__(self, salesDataId, region, division, customerId, transactionDate, transactionAmount):
        self.salesDataId = salesDataId
        self.region = region
        self.division = division
        self.customerId = customerId
        self.transactionDate = transactionDate
        self.transactionAmount = transactionAmount

    @staticmethod
    def to_json(obj: object) -> str:
        return json.dumps(obj.__dict__)

    @staticmethod
    def from_json(json_str: str) -> object:
        inputs = json.loads(json_str)
        obj = SalesDataItem(inputs['salesDataId'], inputs['region'], inputs['division'], inputs['customerId'], inputs['transactionDate'], inputs['transactionAmount'])
        return obj

class SalesRecord(object):
    def __init__(self, transactionDate, transactionAmount):
        self.transactionDate = transactionDate
        self.transactionAmount = transactionAmount

    @staticmethod
    def to_json(obj: object) -> str:
        return json.dumps(obj.__dict__)

    @staticmethod
    def from_json(json_str: str) -> object:
        inputs = json.loads(json_str)
        obj = SalesRecord(inputs['transactionDate'], inputs['transactionAmount'])
        return obj

class GetSalesDataOutputBob(object):
    def __init__(self, region, division, customer, SalesRecords):
        self.region = region
        self.division = division
        self.customer = customer
        self.SalesRecords = SalesRecords
 
    @staticmethod
    def to_json(obj: object) -> str:
        ret_obj = {
            'region': obj.region,
            'division': obj.division,
            'customer': obj.customer,
            'SalesRecords': json.dumps([SalesDataItem.to_json(x) for x in obj.SalesRecords])
        }
        return json.dumps(ret_obj)
 
    @staticmethod
    def from_json(json_str: str) -> object:
        inputs = json.loads(json_str)
        obj = GetSalesDataOutput(inputs['region'], inputs['division'], inputs['customer'], [SalesDataItem.from_json(x) for x in json.loads(inputs['SalesRecords'])])
        return obj