from rest_framework import serializers

from aum.models.stat import Stat


class StatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stat
        fields = ['id', 'date_stat', 'age_min', 'age_min', 'nb_online']


class StatDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stat
        fields = ['id', 'date_stat', 'age_min', 'age_min', 'nb_online']
