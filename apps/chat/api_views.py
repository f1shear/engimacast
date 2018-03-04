from django_filters import rest_framework as filters
from rest_framework import generics

from .filters import ChatRoomFilter
from .models import ChatRoomModel
from .serializers import ChatRoomSerializer


class ChatRoomListView(generics.ListAPIView):
    queryset = ChatRoomModel.objects.all()
    serializer_class = ChatRoomSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ChatRoomFilter


class ChatRoomDetailView(generics.RetrieveAPIView):
    queryset = ChatRoomModel.objects.all()
    serializer_class = ChatRoomSerializer
