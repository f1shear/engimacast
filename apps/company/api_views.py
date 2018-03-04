from django_filters import rest_framework as filters
from rest_framework import generics

from .filters import CompanyFilter, CompanyEventFilter
from .models import CompanyEventModel, CompanyModel
from .serializers import CompanySerializer, CompanyEventSerializer


class CompanyListView(generics.ListAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CompanyFilter


class CompanyDetailView(generics.RetrieveAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer


class CompanyEventListView(generics.ListAPIView):
    queryset = CompanyEventModel.objects.all()
    serializer_class = CompanyEventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CompanyEventFilter


class CompanyEventDetailView(generics.RetrieveAPIView):
    queryset = CompanyEventModel.objects.all()
    serializer_class = CompanyEventSerializer
