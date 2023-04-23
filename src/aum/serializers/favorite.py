from rest_framework import serializers

from aum.models.favorite import Favorite


class CharmListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ['id', 'aum_id']


class FavoriteDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ['id', 'aum_id']
