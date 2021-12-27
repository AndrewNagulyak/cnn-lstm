from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import tweepy
import pandas as pd
import time
from .models import TwitterSet


class TwitterViewSet(viewsets.ViewSet):

    def getTwitterDataByKeyWords(self, request):
        twitter_consumer_key = 'BicCeXWxQIUkEP0B2Efnzjoxe'
        twitter_consumer_secret = 'KX1KSO6pfBDZoxFjfLv2bVQkQkv355SHtY4qDHPwVcm49n3KOm'
        twitter_access_token_key = '1243160586646622209-nsnDeQSehjOhaF2EtXxiVTVf2TSCNS'
        twitter_access_token_secret = 'xgGLyfOFCqMU2NjIY9al1swyH5xk4g9jWCd9XeZbBKg3Z'
        auth = tweepy.OAuthHandler(
            twitter_consumer_key, twitter_consumer_secret)
        auth.set_access_token(twitter_access_token_key,
                              twitter_access_token_secret)
        api = tweepy.API(auth)
        
        untilDate = request.data.get('untilDate')
        queary = request.data.get('queary')
        companyName = request.data.get('companyName')
        tweets_by_word_search(api, queary, companyName)
        return Response('Success')


def tweets_by_word_search(api, word, companyName):
    count = 2
    last_id = -1
    max_tweets = 100
    searched_tweets = []
    tweet_id = []
    tweets = []
    created_at = []
    followers_count = []
    likes = []
    friends_count = []
    retweet_count = []
    df = pd.DataFrame(columns=['tweet_id', 'text',
                      'created_at', 'likes', 'retweet_count', 'followers_count', 'friends_count'])
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        
        try:
            new_tweets = api.search_tweets(q = word,count=count, max_id=str(last_id - 1), lang='en') 
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[0].id
            for i, tweet in enumerate(new_tweets):
                print('Getting tweet: {}'.format(i))
                tweet_id.append(tweet.id)
                tweets.append(tweet.text)
                followers_count.append(tweet.user.followers_count)
                friends_count.append(tweet.user.friends_count)
                created_at.append(tweet.created_at)
                likes.append(tweet.favorite_count)
                retweet_count.append(tweet.retweet_count)
                df.loc[i] = [tweet.id, tweet.text, tweet.created_at,
                             tweet.favorite_count, tweet.retweet_count, tweet.user.followers_count, tweet.user.friends_count]  
                df.to_csv(f'../twitterDataSet/{companyName}.csv', index=False)
                time.sleep(1)
        except tweepy.errors.TweepyException as e:
            print(f"\nPlease wait...proceeding in a few minutes.\n({e})\n")
            time.sleep(2 * 60)
            print('try')
            continue
