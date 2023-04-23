from rest_framework import serializers

from aum.models.contact import Contact


class ContactListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'aum_id']


class ContactDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'aum_id']
