from __future__ import absolute_import, unicode_literals

import datetime
import logging
import time

import dateutil.parser
import pytz
from celery import shared_task

from assets.models import (
    AssetModel, MarketModel, MarketAssetModel,
    PriceHistoryModel, AssetHistoryModel, AssetMediaModel,
    DomainMediaModel
)
from scraper.asset_markets_scraper import extract_markets
from scraper.asset_scraper import extract_assets
from scraper.media_scraper import get_tweets
from scraper.news_scraper import get_articles

SHORT_DELAY = 2
DELAY = 6
LONG_DELAY = 12


def get_usd(value):
    if value:
        value = value.replace('$', '').replace(',', '')
        return value
    else:
        return None


def get_pair(value):
    if value:
        return value.split('/')
    else:
        return None


@shared_task
def add(x, y):
    print("Adding x+y")
    return x + y


@shared_task
def scrape_assets():
    logging.info("Running Assets Scraper")

    try:
        assets = extract_assets()
    except Exception as e:
        logging.error(str(e))
        return

    for asset in assets:
        obj, _ = AssetModel.objects.update_or_create(
            cmc_id=asset.get('id'),
            defaults=dict(symbol=asset.get('symbol'),
                          name=asset.get('name'),
                          trading_volume=asset.get('24h_volume_usd'),
                          recent_cmc_rank=asset.get('rank'),
                          max_supply=asset.get('max_supply'),
                          total_supply=asset.get('total_supply'),
                          circulating_supply=asset.get('available_supply'),
                          market_capital=asset.get('market_cap_usd'),
                          latest_price=get_usd(asset.get('price_usd'))
                          )
        )

        current_dt = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
        # this can be done in model too
        PriceHistoryModel.objects.create(
            asset=obj,
            price=get_usd(asset.get('price_usd')),
            price_at=current_dt
        )
        past_dt = current_dt - datetime.timedelta(hours=1)

        # this can also be done in model
        qs = AssetHistoryModel.objects.filter(asset=obj).order_by('-created_at')
        if qs.count() > 0:
            last_one = qs[0]
            if last_one.created_at <= past_dt:
                AssetHistoryModel.objects.create(
                    asset=obj,
                    price=get_usd(asset.get('price_usd')),
                    cmc_rank=asset.get('rank'),
                    max_supply=asset.get('max_supply'),
                    total_supply=asset.get('total_supply'),
                    circulating_supply=asset.get('available_supply'),
                    market_capital=asset.get('market_cap_usd'),
                    trading_volume=asset.get('24h_volume_usd'),
                )
        else:
            AssetHistoryModel.objects.create(
                asset=obj,
                price=get_usd(asset.get('price_usd')),
                cmc_rank=asset.get('rank'),
                max_supply=asset.get('max_supply'),
                total_supply=asset.get('total_supply'),
                circulating_supply=asset.get('available_supply'),
                market_capital=asset.get('market_cap_usd'),
                trading_volume=asset.get('24h_volume_usd'),
            )


@shared_task
def asset_markets_scraper_dispatcher():
    logging.info("Dispatching Asset Markets Scraper")

    eta = 0
    for asset in AssetModel.objects.all():
        scrape_asset_markets.apply_async((asset.id,), countdown=eta)
        time.sleep(SHORT_DELAY)


@shared_task
def scrape_asset_markets(asset_id):
    asset = AssetModel.objects.get(id=asset_id)
    try:
        info, markets = extract_markets(asset.cmc_id)
    except Exception as e:
        logging.error(str(e))
        return

    asset.website = info.get('website')
    asset.explorer = info.get('explorer')
    asset.asset_type = info.get('asset_type', '')
    asset.save()

    for market_data in markets:
        market, _ = MarketModel.objects.update_or_create(
            name=market_data.get('name')
        )

        MarketAssetModel.objects.update_or_create(
            asset=asset,
            market=market,
            defaults=dict(latest_price=get_usd(market_data.get('price')),
                          volume=get_usd(market_data.get('volume_usd')),
                          pair=market_data.get('pair'))
        )


@shared_task
def social_media_scraper_dispatcher():
    logging.info("Dispatch Social Media Scraper etc: 1 hour")
    eta = 0
    for asset in AssetModel.objects.all():
        scrape_social_media.apply_async((asset.id,), countdown=eta)
        time.sleep(DELAY)


@shared_task
def news_scraper_dispatcher():
    logging.info("Dispatch News Scraper")
    eta = 0
    for asset in AssetModel.objects.all().order_by('-recent_cmc_rank')[0:125]:
        scrape_news.apply_async((asset.id,), countdown=eta)
        time.sleep(DELAY)


@shared_task
def domain_news_scraper_dispatcher():
    logging.info("Dispatch Domain News Scraper")
    eta = 0
    for topic, _ in DomainMediaModel.TOPICS:
        scrape_domain_news.apply_async((topic,), countdown=eta)
        time.sleep(DELAY)


@shared_task
def scrape_social_media(asset_id):
    asset = AssetModel.objects.get(id=asset_id)

    query = "%s %s" % (asset.name, asset.asset_type)
    tweets = get_tweets(query)

    for tweet in tweets:
        AssetMediaModel.objects.update_or_create(
            ref_id=tweet.id_str,
            asset=asset,
            defaults=dict(
                source='twitter.com',
                media_type='social',
                description=tweet.text,
                published_at=dateutil.parser.parse(tweet.created_at)
            )
        )


@shared_task
def scrape_news(asset_id):
    asset = AssetModel.objects.get(id=asset_id)

    query = "%s %s" % (asset.name, asset.asset_type)
    news = get_articles(query)

    for article in news:
        source = None
        if article.get('source'):
            source = article.get('source')['name']
        AssetMediaModel.objects.update_or_create(
            source=source,
            title=article.get('title'),
            asset=asset,
            defaults=dict(
                url=article.get('url'),
                media_type='news',
                description=article.get('description', ''),
                published_at=dateutil.parser.parse(
                    article.get('publishedAt'))
            )
        )


@shared_task
def scrape_domain_news(topic):
    news = get_articles(topic)

    for article in news:
        source = None
        if article.get('source'):
            source = article.get('source')['name']
        DomainMediaModel.objects.update_or_create(
            source=source,
            title=article.get('title'),
            topic=topic,
            published_at=dateutil.parser.parse(
                article.get('publishedAt')),
            defaults=dict(
                url=article.get('url'),
                media_type='news',
                description=article.get('description', '')
            )
        )

    tweets = get_tweets(topic)

    for tweet in tweets:
        DomainMediaModel.objects.update_or_create(
            ref_id=tweet.id_str,
            topic=topic,
            defaults=dict(
                source='twitter.com',
                media_type='social',
                description=tweet.text,
                published_at=dateutil.parser.parse(tweet.created_at)
            )
        )
