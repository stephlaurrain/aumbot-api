from rest_framework import serializers

from aum.models.charm import Charm


class CharmListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charm
        fields = ['id', 'aum_id', 'date_charm']


class CharmDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charm
        fields = ['id', 'aum_id', 'date_charm']
