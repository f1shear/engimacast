from django.urls import path

from . import views

urlpatterns = [
    path('assistant/', views.AssistantView.as_view()),
    path('media/', views.MediaView.as_view()),
    path('tools/', views.ToolsView.as_view())
]
