from rest_framework import serializers

from aum.models.ban import Ban


class BanListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ban
        fields = ['id', 'aum_id','done']


class BanDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ban
        fields = ['id', 'aum_id','done']
