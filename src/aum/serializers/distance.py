from rest_framework import serializers

from aum.models.distance import Distance


class DistanceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distance
        fields = ['id', 'city', 'km']


class DistanceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distance
        fields = ['id', 'city', 'km']
