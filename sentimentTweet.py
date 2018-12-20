import tweepy
import csv
from textblob import TextBlob


consumer_key = 'mIChfLYa0b9KPI2kzhNMJORvD'
consumer_secret = 'fq9VINTa2Jnjs4JB3hfWB5FESvVbDWEuoGWgyR4Gwbwai7JrlZ'

access_token = '3024123880-aoYgpvlxRK4BadEbPDZCbU10Hn4g6fAEG2Tuf3F'
access_token_secret = 'WaGo9FNmyg72y9XXqbhmMdc1vrzrYw0Rw5GPrdNpNDRBA'

polarity_threshold = 5
csv_file="tweet_results.csv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

file = open(csv_file, "a")

list_polarity = []
list_test = []

with file:
	writer = csv.writer(file)

	for tweet in public_tweets:
		print(tweet.text)
		analysis = TextBlob(tweet.text)
		list_test.append(tweet.text)

		if analysis.sentiment.polarity > 5:

			#list_polarity.append("positive")
			label= "positve"
		else:
			label="negetive"
			#list_polarity.append("negetive")
		writer.writerow([tweet.text,label])

file.close()

