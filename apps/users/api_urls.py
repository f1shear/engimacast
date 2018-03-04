from django.urls import path

from . import api_views

urlpatterns = [
    path('users/', api_views.UserListView.as_view()),
    path('users/<:int>/', api_views.UserDetailView.as_view()),
]
