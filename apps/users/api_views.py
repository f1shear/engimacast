from django_filters import rest_framework as filters
from rest_framework import generics

from .filters import UserFilter
from .models import UserModel
from .serializers import UserSerializer


class UserListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserFilter


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
