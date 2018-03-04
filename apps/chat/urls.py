from django.urls import path

from . import views

urlpatterns = [
    path('rooms/', views.ChatRoomListView.as_view()),
    path('rooms/<int:pk>/', views.ChatRoomDetailView.as_view()),
    path('rooms/global/', views.ChatRoomGlobalView.as_view())
]
