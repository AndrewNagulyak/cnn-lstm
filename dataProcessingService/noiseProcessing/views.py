from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import tweepy
import pandas as pd
import time
import re
import string
from nltk.stem import PorterStemmer
from .models import TwitterProcessingSet


class TwitterProcessingViewSet(viewsets.ViewSet):

    def processTwitterData(self, request):
        companyName = request.data.get('companyName')
        processTweets(companyName)
        return Response('Success')

regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"
                                u"\U0001F300-\U0001F5FF"
                                u"\U0001F680-\U0001F6FF"
                                u"\U0001F1E0-\U0001F1FF"
                                u"\U00002500-\U00002BEF"
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"
                                u"\u3030"
                                "]+", flags=re.UNICODE)
def processTweets(companyName):
    tweets = pd.read_csv(
        f'../twitterDataSet/{companyName}.csv')
    for index, row in tweets.iterrows():
        tweets.loc[index, "text"] = processTweetText(
            tweets.loc[index, "text"])
        tweets.loc[index, "text"] = removeComaSymbols(
            tweets.loc[index, "text"])
        tweets.loc[index, "text"] = stemmingTweetText(
            tweets.loc[index, "text"])
        tweets.to_csv(
            f'../twitterProcessingDataSets/{companyName}.csv', index=False)


def processTweetText(tweet):
    tweet = regrex_pattern.sub(r'', tweet)
    tweet = re.sub(r'\&\w*;', '', tweet)
    tweet = tweet.replace(r'[^\x00-\x7F]+', '')
    tweet = tweet.lower()
    tweet = re.sub(r'https?:\/\/.*\/\w*', '', tweet)
    tweet = re.sub(r'#\w*', '', tweet)
    tweet = re.sub(r'\b\w{1,2}\b', '', tweet)
    tweet = re.sub('@[^\s]+', '', tweet)
    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'\s\s+', ' ', tweet)
    tweet = tweet.lstrip(' ')
    tweet = ''.join(c for c in tweet if c <= '\uFFFF')
    return tweet


def removeComaSymbols(tweet):
    newTweet = [char for char in list(
        tweet) if char not in string.punctuation]
    newTweet = ''.join(newTweet)
    return ' '.join([word for word in newTweet.lower().split() if word.lower()])


def stemmingTweetText(tokens):
    stemmer = PorterStemmer()
    x = [stemmer.stem(w) for w in tokens]
    return ''.join(x)
