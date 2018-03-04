from django.urls import path

from . import api_views

urlpatterns = [
    # api
    path('assets/', api_views.AssetListView.as_view()),
    path('assets/<int:pk>/', api_views.AssetDetailView.as_view()),

    path('assets/<int:asset_id>/media/', api_views.AssetMediaListView.as_view()),
    path('assets/<int:asset_id>/media/<int:pk>/', api_views.AssetMediaDetailView.as_view()),

    path('domain-media/', api_views.DomainMediaListView.as_view()),
    path('domain-media/<int:pk>/', api_views.DomainMediaDetailView.as_view()),

    path('assets/<int:asset_id>/media/<int:media_id>/reactions/', api_views.MediaReactionListView.as_view()),
    path('assets/<int:asset_id>/media/<int:media_id>/reactions/<int:pk>/', api_views.MediaReactionDetailView.as_view()),

    path('assets/<int:asset_id>/votes/', api_views.AssetVoteListView.as_view()),
    path('assets/<int:asset_id>/votes/<int:pk>/', api_views.AssetVoteDetailView.as_view()),

    path('markets/', api_views.MarketListView.as_view()),
    path('markets/<int:pk>/', api_views.MarketDetailView.as_view()),

    path('assets-markets/', api_views.MarketAssetListView.as_view()),
    path('assets-markets/<int:pk>/', api_views.MarketAssetDetailView.as_view()),

    path('assets/<int:asset_id>/history/', api_views.AssetHistoryListView.as_view()),

    path('price-history/', api_views.PriceHistoryListView.as_view()),
    path('price-future/', api_views.PriceFutureListView.as_view()),

]
