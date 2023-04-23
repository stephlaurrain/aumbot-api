from rest_framework import serializers

from aum.models.visit import Visit


class VisitListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ['id',  'aum_id',
                    'username',
                    'city',
                    'distance',
                    'age',
                    'title',
                    'measurement',
                    'nb_photo',
                    'desc',
                    'shopping',
                    'crack',
                    'cant_stand',
                    'popularity',
                    'hot',
                    'score',
                    'date_visit',
                    'date_first_visit',
                    'full_desc',
                    'full_shopping']


class VisitDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ['id', 
                    'aum_id',
                    'username',
                    'city',
                    'distance',
                    'age',
                    'title',
                    'measurement',
                    'nb_photo',
                    'desc',
                    'shopping',
                    'crack',
                    'cant_stand',
                    'popularity',
                    'hot',
                    'score',
                    'date_visit',
                    'date_first_visit',
                    'full_desc',
                    'full_shopping']

