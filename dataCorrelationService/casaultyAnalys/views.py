from rest_framework import viewsets
from rest_framework.response import Response
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from decimal import *
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tsa.stattools import adfuller


class CasaultyViewSet(viewsets.ViewSet):

    def getCasaultyAnalys(self, request):
        data = request.data
        companyName = data.get('companyName')
        twitterTimeSerias = pd.read_csv(
            f'../emotionalDataSets/{companyName}.csv')
        priceTimeSeria = pd.read_csv(
            f'../financeDataSet/{companyName}.csv', usecols=["Close"])
        twitterTimeSerias['Close'] = priceTimeSeria

        for i in twitterTimeSerias:
            try:
                res = adfuller(
                    twitterTimeSerias[i])
                if(res[1] > 0.05):
                    print(f"{i} не є стаціонарною змінною")
                else:
                    print(f"{i} є стаціонарною змінною")
            except:
                continue

        for i in twitterTimeSerias:
            try:
                print(i)
                print('\n')
                res = grangercausalitytests(twitterTimeSerias[[i, 'Close']], maxlag=1)
                print(res[1][0]['ssr_ftest'][1])
                if(res[1][0]['ssr_ftest'][1] > 0.7):
                    twitterTimeSerias = twitterTimeSerias.drop(i, axis=1)
            except:
                continue


        twitterTimeSerias.to_csv(
            f'../twitterCasaultyDataSet/{companyName}.csv', index=False)
        return Response(request.data.get('companyName'))
