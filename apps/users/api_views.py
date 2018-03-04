
from rest_framework import generics


from .models import  UserModel
from .serializers import UserSerializer

from django_filters import rest_framework as filters

from .filters import  UserFilter


class UserListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserFilter


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

