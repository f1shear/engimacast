from __future__ import absolute_import, unicode_literals

from celery import Celery

# set the default Django settings module for the 'celery' program.

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


ONE_MIN = 60.0

ONE_HOUR = ONE_MIN * 60.0

app.conf.beat_schedule = {

    'scrape-assets': {
        'task': 'scraper.tasks.scrape_assets',
        'schedule': ONE_MIN * 10,  # ever 10 minutes
    },

    'scrape-asset-markets': {
        'task': 'scraper.tasks.asset_markets_scraper_dispatcher',
        'schedule': ONE_HOUR * 2.1,  # every 2 hours
    },
    'scrape-media': {
        'task': 'scraper.tasks.social_media_scraper_dispatcher',
        'schedule': ONE_HOUR * 3.1,  # every 3 hour
    },
    'scrape-news': {
        'task': 'scraper.tasks.news_scraper_dispatcher',
        'schedule': ONE_HOUR * 5,  # every 5 hours
    },
    'scrape-domain-news': {
        'task': 'scraper.tasks.domain_news_scraper_dispatcher',
        'schedule': ONE_HOUR * 1,  # every 1 hour
    },
}
