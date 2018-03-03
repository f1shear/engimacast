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
    PriceFutureModel,
    DomainMediaModel
)


@admin.register(AssetModel)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('cmc_id', 'company', 'asset_type', 'name', 'website', 'trading_volume',
                    'circulating_supply', 'latest_price', 'max_price',
                    'min_price', 'created_at', 'updated_at')


@admin.register(AssetMediaModel)
class AssetMediaAdmin(admin.ModelAdmin):
    list_display = ('asset', 'ref_id', 'published_at', 'source', 'media_type', 'title', 'url',
                    'description', 'sentiment_score', 'backlinks_count',
                    'scam_score', 'fud_score', 'created_at',)


@admin.register(DomainMediaModel)
class DomainMediaAdmin(admin.ModelAdmin):
    list_display = ('topic', 'ref_id', 'published_at', 'source', 'media_type', 'title', 'url',
                    'description', 'sentiment_score', 'backlinks_count',
                    'scam_score', 'fud_score', 'created_at',)


@admin.register(MediaReactionModel)
class MediaReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'media', 'reaction', 'created_at', )


@admin.register(AssetVoteModel)
class AssetVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'asset', 'position', 'sentiment', 'created_at', )


@admin.register(MarketModel)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'market_type',
                    'website', 'trade_volume', )


@admin.register(MarketAssetModel)
class MarketAssetAdmin(admin.ModelAdmin):
    list_display = ('market', 'asset', 'latest_price', 'volume', 'pair', )


@admin.register(AssetHistoryModel)
class AssetHistoryAdmin(admin.ModelAdmin):
    list_display = ('asset', 'price', 'popularity_score',
                    'cmc_rank', 'circulating_supply', 'max_supply',
                    'trading_volume', 'created_at', )


@admin.register(PriceHistoryModel)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('asset', 'price', 'price_at', )


@admin.register(PriceFutureModel)
class PriceFutureAdmin(admin.ModelAdmin):
    list_display = ('asset', 'price', 'price_at', )
