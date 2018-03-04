

import django_filters

from .models import (
    AssetModel,
    AssetMediaModel,
    DomainMediaModel,
    MediaReactionModel,
    AssetVoteModel,
    MarketModel,
    MarketAssetModel,
    AssetHistoryModel,
    PriceHistoryModel,
    PriceFutureModel
)



class AssetFilter(django_filters.FilterSet):
    class Meta:
        model = AssetModel
        fields = {
            'name': ['exact', 'icontains', ],
            'symbol': ['exact' ],
            'company': ['exact'],
            'asset_type': ['exact']
        }


class AssetMediaFilter(django_filters.FilterSet):

    class Meta:
        model = AssetMediaModel
        fields = {
            'asset': ['exact', ],
            'media_type': ['exact', ]
        }


class DomainMediaFilter(django_filters.FilterSet):

    class Meta:
        model = DomainMediaModel
        fields = {
            'topic': ['exact',],
            'media_type': ['exact', ]
        }


class MediaReactionFilter(django_filters.FilterSet):

    class Meta:
        model = MediaReactionModel
        fields = {
            'user': ['exact'],
            'media': ['exact'],
        }


class AssetVoteFilter(django_filters.FilterSet):

    class Meta:
        model = AssetVoteModel
        fields = {
            'user': ['exact'],
            'asset': ['exact']
        }


class MarketFilter(django_filters.FilterSet):

    class Meta:
        model = MarketModel
        fields = {
            'name': ['icontains', 'exact'],
            'market_type': ['exact'],
        }


class MarketAssetFilter(django_filters.FilterSet):

    class Meta:
        model = MarketAssetModel
        fields = {
            'market': ['exact'],
            'asset': ['exact']
        }


class AssetHistoryFilter(django_filters.FilterSet):

    class Meta:
        model = AssetHistoryModel
        fields = {
            'asset': ['exact']
        }


class PriceHistoryFilter(django_filters.FilterSet):

    class Meta:
        model = PriceHistoryModel
        fields = {
            'asset': ['exact']
        }


class PriceFutureFilter(django_filters.FilterSet):

    class Meta:
        model = PriceFutureModel
        fields = {
            'asset': ['exact']
        }
