from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import tweepy
import pandas as pd
import time
from .models import EmotionalSet
import re
from urllib.error import HTTPError
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class EmotionalViewSet(viewsets.ViewSet):

    def processEmotionalData(self, request):
        companyName = request.data.get('companyName')
        tweets = pd.read_csv(
            f'../twitterProcessingDataSets/{companyName}.csv')
        for index, row in tweets.iterrows():
            # print(tweets.loc[index, "text"])
            tweets.loc[index, "text"] = vaderSantimatesText(tweets.loc[index, "text"])
        tweets.to_csv(
            f'../emotionalDataSets/{companyName}.csv', index=False)
        return Response('Success')


def vaderSantimatesText(text):

    vaiderEstimate = SentimentIntensityAnalyzer()
    estimate = vaiderEstimate.polarity_scores(text)
    # print(text)
    # print("Оцінка тексту:", estimate)
    # print("Текст був оцінений як ", estimate['neg']*100, "% Негативний")
    # print("Текст був оцінений як ", estimate['neu']*100, "% Нейтральний")
    # print("Текст був оцінений як ", estimate['pos']*100, "% Позитивний")
    # print("Загальна оцінка", end=" ")
    # if estimate['compound'] >= 0.05:
    #     print("Позитивний")
    # elif estimate['compound'] <= - 0.05:
    #     print("Негативний")
    # else:
    #     print("Нейтральний")
    return estimate['compound']
