from django.contrib import admin

# Register your models here.


from .models import (
    AssetModel,
    AssetMediaModel,
    MediaReactionModel,
    AssetVoteModel,
    MarketModel,
    MarketAssetModel,
    AssetHistoryModel,
    PriceHistoryModel,
    PriceFutureModel
)


@admin.register(AssetModel)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('company', 'asset_type', 'name', 'website', 'volume',
                    'circulating_supply', 'latest_price', 'max_price',
                    'min_price', 'created_on', 'updated_on')


@admin.register(AssetMediaModel)
class AssetMediaAdmin(admin.ModelAdmin):
    list_display = ('asset', 'source', 'media_type', 'title', 'url',
                    'description', 'sentiment_score', 'backlinks_count',
                    'scam_score', 'fud_score', 'created_on', 'updated_on')


@admin.register(MediaReactionModel)
class MediaReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'media', 'reaction', 'created_on', )


@admin.register(AssetVoteModel)
class AssetVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'asset', 'position', 'sentiment', 'created_on', )


@admin.register(MarketModel)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'market_type',
                    'website', 'trade_volume', )


@admin.register(MarketAssetModel)
class MarketAssetAdmin(admin.ModelAdmin):
    list_display = ('market', 'asset', 'latest_price',
                    'latest_rate', 'volume', 'exchange_asset', )


@admin.register(AssetHistoryModel)
class AssetHistoryAdmin(admin.ModelAdmin):
    list_display = ('asset', 'price', 'popularity_score',
                    'cmc_rank', 'circulating_supply', 'max_supply',
                    'trading_volume', 'updated_on', )


@admin.register(PriceHistoryModel)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('asset', 'price', 'price_on', )


@admin.register(PriceFutureModel)
class PriceFutureAdmin(admin.ModelAdmin):
    list_display = ('asset', 'price', 'price_on', )
