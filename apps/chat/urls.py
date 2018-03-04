from django.urls import path

from . import api_views

urlpatterns = [
    path('chat-rooms/', api_views.ChatRoomListView.as_view()),
    path('chat-rooms/<int:pk>/', api_views.ChatRoomDetailView.as_view())
]