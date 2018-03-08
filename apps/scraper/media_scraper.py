import os

import twitter


def get_twitter_client():
    client = twitter.Api(
        consumer_key=os.environ.get('TWITTER_CONSUMER_KEY'),
        consumer_secret=os.environ.get('TWITTER_CONSUMER_SECRET'),
        access_token_key=os.environ.get('TWITTER_ACCESS_TOKEN_KEY'),
        access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))
    return client


def get_tweets(topic):
    client = get_twitter_client()
    results = client.GetSearch(
        raw_query="q=%s&result_type=recent&count=100" % topic)
    processed = []
    for tweet in results:
        if tweet.lang == "en":
            processed.append(tweet)
    return processed


if __name__ == '__main__':
    for tweet in get_tweets('nexus coin'):
        print(tweet.text)
