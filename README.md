

# About

  -  Scrapes current price and statistics of cryptocurrencies from CoinMarketCap
  -  Reads twitter feeds
  -  Reads news via news api
  -  Frontend displays information about retrieved price statistics, twitter feeds , news about each currency 


# Stack

  -  Django
  -  Vuejs
  -  Bootstrap


# Install

    $ virtualenv -p python 3.6 env

    $ source env/bin/activate

    $ pip install -r requirements.txt


Note: Please modify requirements.txt file as per your local requirements


# Environment variables

- DJANGO_SETTINGS_MDOULE
- NEWS_API_KEY
- TWITTER_CONSUMER_KEY
- TWITTER_CONSUMER_SECRET
- TWITTER_ACCESS_TOKEN_KEY
- TWITTER_ACCESS_TOKEN_SECRET


# Dev settings

- DATABASES


# Run DJANGO

- python manage.py runserver --settings project.local_settings


# Run Celery and Celery Beat

- celery -A project worker -l info --purge

- celery -A project beat


# Purge celery messages

- celery purge -f

