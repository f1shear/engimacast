from __future__ import absolute_import, unicode_literals

import datetime
import logging
import pytz
import dateutil.parser
from celery import shared_task

from assets.models import (
    AssetModel, MarketModel, MarketAssetModel,
    PriceHistoryModel, AssetHistoryModel, AssetMediaModel
)
from scraper.asset_markets_scraper import extract_markets
from scraper.asset_scraper import extract_assets
from scraper.media_scraper import get_tweets
from scraper.news_scraper import get_articles


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
    logging.info("Running Assets Scraper: Every 5 minutes")
    assets = extract_assets()
    for asset in assets:
        logging.info('Reading asset %s' % asset['name'])
        obj, _ = AssetModel.objects.update_or_create(
            name=asset.get('name'),
            defaults=dict(symbol=asset.get('symbol'),
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
    logging.info("Dispatch Market Scraper: Every 1 hour")

    eta = 0
    for asset in AssetModel.objects.all():
        scrape_asset_markets.apply_async((asset.id), countdown=eta)
        eta += 5

@shared_task
def scrape_asset_markets(asset_id):
    asset = AssetModel.objects.get(id=asset_id)
    info, markets = extract_markets(asset.name)

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
def media_scraper_dispatcher():
    logging.info("Dispatch Market Scraper: Every 1 hour")
    eta = 0
    for asset in AssetModel.objects.all():
        scrape_media.apply_async((asset.id, ), countdown=eta)
        eta += 5

@shared_task
def scrape_media(asset_id):

    asset = AssetModel.objects.get(id=asset_id)
    logging.info("Running Media Scraper for %s" % asset.name)
    tweets = get_tweets(asset.name)
    news = get_articles(asset.name)

    logging.info("Found %s tweets" % len(tweets))
    logging.info("Found %s news" % len(news))

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
