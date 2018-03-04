from django.urls import path

from . import api_views

urlpatterns = [
    path('companies/', api_views.CompanyListView.as_view()),
    path('companies/<int:pk>/', api_views.CompanyDetailView.as_view()),
    path('companies-events/', api_views.CompanyEventListView.as_view()),
    path('companies-events/<int:pk>/', api_views.CompanyEventDetailView.as_view()),
]
