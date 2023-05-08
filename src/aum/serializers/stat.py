from rest_framework import serializers

from aum.models.stat import Stat


class StatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stat
        fields = ['id', 'date_stat', 'age_min', 'age_max', 'nb_online', 'dist']


class StatDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stat
        fields = ['id', 'date_stat', 'age_min', 'age_max', 'nb_online', 'dist']
