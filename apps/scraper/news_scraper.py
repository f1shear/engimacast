

import os
import logging
from newsapi import NewsApiClient


API_KEY = os.environ.get("NEWS_API_KEY")


def get_articles(topic, headlines=False):

    newsapi = NewsApiClient(api_key=API_KEY)

    if not headlines:
        articles = newsapi.get_everything(
            q=topic,
            language='en',
            sort_by='relevancy',
            page_size=100)
    else:
        articles = newsapi.get_top_headlines(
            q=topic,
            language='en',
            page_size=100)
    return articles['articles']


if __name__ == '__main__':
    articles = get_articles('bitcoin')
    for article in articles['articles']:
        for key in article:
            print(key)
        break
