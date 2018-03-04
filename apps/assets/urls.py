from django.urls import path

from . import views

urlpatterns = [
    # api
    path('', views.AssetListView.as_view()),
    path('<int:pk>/', views.AssetDetailView.as_view()),

]
