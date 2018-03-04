from rest_framework import serializers

from .models import (
    CompanyModel,
    CompanyEventModel
)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'


class CompanyEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyEventModel
        fields = '__all__'
