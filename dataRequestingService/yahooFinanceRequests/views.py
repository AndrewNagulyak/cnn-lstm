from rest_framework import viewsets
from rest_framework.response import Response
import time
import datetime

import pandas as pd



class StockViewSet(viewsets.ViewSet):

    def getStockDataByKeyWords(self, request):
        data = request.data
        companyName = data.get('companyName')
        period1 = data.get('period1')
        period2 = data.get('period2')
        apiUrlQueary = 'https://query1.finance.yahoo.com/v7/finance/download/' + companyName + '?period1=' + period1 + '&period2=' + period2 + '&interval=1d&events=history&includeAdjustedClose=true'
        df = pd.read_csv(apiUrlQueary)
        df.to_csv('../financeDataSet/'+companyName+'.csv')
        return Response(request.data.get('companyName'))
