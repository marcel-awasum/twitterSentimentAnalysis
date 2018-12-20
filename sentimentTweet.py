import tweepy
from textblob import TextBlob


consumer_key = 'mIChfLYa0b9KPI2kzhNMJORvD'
consumer_secret = 'fq9VINTa2Jnjs4JB3hfWB5FESvVbDWEuoGWgyR4Gwbwai7JrlZ'

access_token = '3024123880-aoYgpvlxRK4BadEbPDZCbU10Hn4g6fAEG2Tuf3F'
access_token_secret = 'WaGo9FNmyg72y9XXqbhmMdc1vrzrYw0Rw5GPrdNpNDRBA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
