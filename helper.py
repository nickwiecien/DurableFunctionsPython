import json

class GetSalesDataInput:
  def __init__(self, division, region):
    self.division = division
    self.region = region

  def to_json(self):
    return json.dumps(self.__dict__)

class GetSalesDataOutput:
    def __init__(self, region, division, customerId, monthlySalesTotal):
        self.region = region
        self.division = division
        self.customerId = customerId
        self.monthlySalesTotal = monthlySalesTotal

    def to_json(self):
        return json.dumps(self.__dict__)


class ProcessDataInput:
    def __init__(self, region, division, customerId, runId, monthlySalesTotal):
        self.region = region
        self.division = division
        self.customerId = customerId
        self.runId = runId
        self.monthlySalesTotal = monthlySalesTotal
    
    def to_json(self):
        return json.dumps(self.__dict__)

class ProcessDataResult:
    def __init__(self, region, division, customerId, salesAnomalyCalculation, rowKey, partitionKey):
        self.region = region
        self.division = division
        self.customerId = customerId
        self.salesAnomalyCalculation = salesAnomalyCalculation
        self.rowKey = rowKey
        self.partitionKey = partitionKey

    def to_json(self):
        return json.dumps(self.__dict__)

class SalesAggregateInput:
    def __init__(self, regions, divisions):
        self.regions = regions
        self.divisions = divisions

    def to_json(self):
        return json.dumps(self.__dict__)
        
class SalesAnomaly:
    def __init__(self, salesAnomalyId, runId, region, division, customerId, anomalyCalculationResult):
        self.salesAnomalyId = salesAnomalyId
        self.runId = runId
        self.region = region
        self.division = division
        self.customerId = customerId
        self.anomalyCalculationResult = anomalyCalculationResult

    def to_json(self):
        return json.dumps(self.__dict__)

class SalesDataItem:
    def __init__(self, salesDataId, region, division, customerId, transactionDate, transactionAmount):
        self.salesDataId = salesDataId
        self.region = region
        self.division = division
        self.customerId = customerId
        self.transactionDate = transactionDate
        self.transactionAmount = transactionAmount

    def to_json(self):
        return json.dumps(self.__dict__)

class SalesRecord:
    def __init__(self, transactionDate, transactionAmount):
        self.transactionDate = transactionDate
        self.transactionAmount = transactionAmount

    def to_json(self):
        return json.dumps(self.__dict__)