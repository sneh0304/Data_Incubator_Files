import tweepy
import json
import jsonpickle

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#values pf q for searching tweets
a = ['#COVID-19', '#CoronaLockdown', '#CoronavirusOutbreak', '#Coronavirus', '#CoronairusPandemic', '#CoronavirusOutbreakindia', '#CoronaUpdate', '#CoronaLockdown']

tweets = []
for tweet in tweepy.Cursor(api.search, q = "#CoronaLockdown", tweet_mode = 'extended').items():
    tweets.append(tweet._json)
    

with open('tweets.json', 'a', encoding='utf8') as f:
    for tweet in tweets:
        f.write(jsonpickle.encode(tweet, unpicklable=False) + ',\n')