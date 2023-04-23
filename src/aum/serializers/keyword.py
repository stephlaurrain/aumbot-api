from rest_framework import serializers

from aum.models.keyword import Keyword


class KeywordListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ['id', 'word', 'weight']


class KeywordDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ['id', 'word', 'weight']
