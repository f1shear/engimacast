from rest_framework import serializers

from .models import (
    AssetModel,
    AssetMediaModel,
    DomainMediaModel,
    MediaReactionModel,
    AssetVoteModel,
    MarketModel,
    MarketAssetModel,
    AssetHistoryModel,
    PriceHistoryModel,
    PriceFutureModel
)


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AssetModel


class AssetMediaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AssetMediaModel


class DomainMediaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DomainMediaModel


class MediaReactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MediaReactionModel


class MediaReactionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('media', 'reaction',)
        model = MediaReactionModel

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return MediaReactionModel.objects.create(**validated_data)


class AssetVoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AssetVoteModel


class AssetVoteWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('asset', 'position', 'sentiment',)
        model = AssetVoteModel

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return AssetVoteModel.objects.create(**validated_data)


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MarketModel


class MarketAssetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MarketAssetModel


class AssetHistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AssetHistoryModel


class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PriceHistoryModel


class PriceFutureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PriceFutureModel
