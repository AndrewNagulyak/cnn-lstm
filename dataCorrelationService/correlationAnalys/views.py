from rest_framework import viewsets
from rest_framework.response import Response
import time
import datetime

import pandas as pd



class CorrelationViewSet(viewsets.ViewSet):

    def getCorrelationAnalys(self, request):
        data = request.data
        companyName = data.get('companyName')
        twitterTimeSerias = pd.read_csv(f'../twitterCasaultyDataSet/{companyName}.csv')
        twitterTimeSerias = twitterTimeSerias.drop(['created_at'], axis=1)
        priceTimeSeria = pd.read_csv(
        f'../financeDataSet/{companyName}.csv', usecols=["Close"])
        for i in twitterTimeSerias:
            res = twitterTimeSerias[i].corr(other = priceTimeSeria['Close'], method='pearson')
            twitterTimeSerias.loc[:,i] = twitterTimeSerias.loc[:,i] * abs(res) * 100
        twitterTimeSerias.to_csv(f'../twitterCorelatedDataSet/{companyName}.csv', index=False)
        print(twitterTimeSerias)
        return Response(request.data.get('companyName'))
