import logging

from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework import permissions

from core.permissions import IsOwnerOrReadOnly
from .filters import (
    AssetFilter,
    AssetMediaFilter,
    DomainMediaFilter,
    MediaReactionFilter,
    AssetVoteFilter,
    MarketFilter,
    MarketAssetFilter,
    AssetHistoryFilter,
    PriceHistoryFilter,
    PriceFutureFilter
)
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
from .serializers import (
    AssetSerializer,
    AssetMediaSerializer,
    DomainMediaSerializer,
    MediaReactionSerializer,
    MediaReactionWriteSerializer,
    AssetVoteSerializer,
    AssetVoteWriteSerializer,
    MarketSerializer,
    MarketAssetSerializer,
    AssetHistorySerializer,
    PriceHistorySerializer,
    PriceFutureSerializer

)


class AssetListView(generics.ListAPIView):
    queryset = AssetModel.objects.all()
    serializer_class = AssetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AssetFilter
    permission_classes = None


class AssetDetailView(generics.RetrieveAPIView):
    queryset = AssetModel.objects.all()
    serializer_class = AssetSerializer
    permission_classes = None


class AssetMediaListView(generics.ListAPIView):
    serializer_class = AssetMediaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AssetMediaFilter
    permission_classes = None

    def get_asset(self, asset_id):
        return get_object_or_404(AssetModel, id=asset_id)

    def get_queryset(self):
        asset_id = self.kwargs.get('asset_id')
        return AssetMediaModel.objects.filter(
            asset=self.get_asset(asset_id)
        )


class AssetMediaDetailView(generics.RetrieveAPIView):
    serializer_class = AssetMediaSerializer
    permission_classes = None

    def get_asset(self, asset_id):
        return get_object_or_404(AssetModel, id=asset_id)

    def get_queryset(self):
        asset_id = self.kwargs.get('asset_id')
        return AssetMediaModel.objects.filter(
            asset=self.get_asset(asset_id)
        )


class DomainMediaListView(generics.ListAPIView):
    queryset = DomainMediaModel.objects.all()
    serializer_class = DomainMediaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DomainMediaFilter
    permission_classes = None


class DomainMediaDetailView(generics.RetrieveAPIView):
    queryset = DomainMediaModel.objects.all()
    serializer_class = DomainMediaSerializer
    permission_classes = None


class MediaReactionListView(generics.ListCreateAPIView):
    """ write too """
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MediaReactionFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_media(self, obj_id):
        logging.error('getting media')
        return get_object_or_404(AssetMediaModel, id=obj_id)

    def get_queryset(self):
        logging.error('getting queryset')
        media_id = self.kwargs.get('media_id')
        media = self.get_media(media_id)
        return MediaReactionModel.objects.filter(
            media=media)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MediaReactionSerializer
        return MediaReactionWriteSerializer


class MediaReactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ write too """
    permission_classes = (IsOwnerOrReadOnly,)

    def get_media(self, obj_id):
        logging.error('getting media')
        return get_object_or_404(AssetMediaModel, id=obj_id)

    def get_queryset(self):
        logging.error('getting queryset')
        media_id = self.kwargs.get('media_id')
        media = self.get_media(media_id)
        return MediaReactionModel.objects.filter(
            media=media)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MediaReactionSerializer
        return MediaReactionWriteSerializer


class AssetVoteListView(generics.ListCreateAPIView):
    """ write too """
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AssetVoteFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_asset(self, asset_id):
        return get_object_or_404(AssetModel, id=asset_id)

    def get_queryset(self):
        asset_id = self.kwargs.get('asset_id')
        return AssetVoteModel.objects.filter(
            asset=self.get_asset(asset_id)
        )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AssetVoteSerializer
        return AssetVoteWriteSerializer


class AssetVoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ write too"""
    permission_classes = (IsOwnerOrReadOnly,)

    def get_asset(self, asset_id):
        return get_object_or_404(AssetModel, id=asset_id)

    def get_queryset(self):
        asset_id = self.kwargs.get('asset_id')
        return AssetVoteModel.objects.filter(
            asset=self.get_asset(asset_id)
        )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AssetVoteSerializer
        return AssetVoteWriteSerializer


class MarketListView(generics.ListAPIView):
    queryset = MarketModel.objects.all()
    serializer_class = MarketSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MarketFilter


class MarketDetailView(generics.RetrieveAPIView):
    queryset = MarketModel.objects.all()
    serializer_class = MarketSerializer


class MarketAssetListView(generics.ListAPIView):
    queryset = MarketAssetModel.objects.all()
    serializer_class = MarketAssetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MarketAssetFilter


class MarketAssetDetailView(generics.RetrieveAPIView):
    queryset = MarketAssetModel.objects.all()
    serializer_class = MarketAssetSerializer


class AssetHistoryListView(generics.ListAPIView):
    serializer_class = AssetHistorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AssetHistoryFilter

    def get_asset(self, asset_id):
        return get_object_or_404(AssetModel, id=asset_id)

    def get_queryset(self):
        asset_id = self.kwargs.get('asset_id')
        return AssetHistoryModel.objects.filter(
            asset=self.get_asset(asset_id)
        )


class PriceHistoryListView(generics.ListAPIView):
    queryset = PriceHistoryModel.objects.all()
    serializer_class = PriceHistorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PriceHistoryFilter


class PriceFutureListView(generics.ListAPIView):
    queryset = PriceFutureModel.objects.all()
    serializer_class = PriceFutureSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PriceFutureFilter
