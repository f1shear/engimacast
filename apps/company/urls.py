from django.urls import path

from . import views

urlpatterns = [
    path('', views.CompanyListView.as_view()),
    path('<int:pk>/', views.CompanyDetailView.as_view()),
]
