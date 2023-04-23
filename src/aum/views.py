import logging

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from aum.permissions import IsAdminAuthenticated, IsBotAuthenticated
from aum.models.visit import Visit

#ici ajoute modeles pour migration

from aum.models.ban import Ban
from aum.models.charm import Charm
from aum.models.contact import Contact
from aum.models.distance import Distance
from aum.models.favorite import Favorite
from aum.models.keyword import Keyword
from aum.models.visit import Visit

from aum.serializers.visit import VisitDetailSerializer, VisitListSerializer
from aum.serializers.ban import BanDetailSerializer, BanListSerializer
from aum.serializers.charm import CharmDetailSerializer, CharmListSerializer
from aum.serializers.contact import ContactDetailSerializer, ContactListSerializer
from aum.serializers.distance import DistanceDetailSerializer, DistanceListSerializer
from aum.serializers.favorite import FavoriteDetailSerializer, FavoriteListSerializer
from aum.serializers.keyword import KeywordDetailSerializer, KeywordListSerializer



class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class AdminVisitViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = VisitListSerializer
    detail_serializer_class = VisitDetailSerializer
    queryset = Visit.objects.all()
    permission_classes = [IsAdminAuthenticated]


class VisitViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = VisitListSerializer
    detail_serializer_class = VisitDetailSerializer
    queryset = Visit.objects.all()
    permission_classes = [IsBotAuthenticated]


class AdminBanViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = BanListSerializer
    detail_serializer_class = BanDetailSerializer
    queryset = Ban.objects.all()
    permission_classes = [IsAdminAuthenticated]


class BanViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = BanListSerializer
    detail_serializer_class = BanDetailSerializer
    queryset = Ban.objects.all()
    permission_classes = [IsBotAuthenticated]


class AdminCharmViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CharmListSerializer
    detail_serializer_class = CharmDetailSerializer
    queryset = Charm.objects.all()
    permission_classes = [IsAdminAuthenticated]


class CharmViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CharmListSerializer
    detail_serializer_class = CharmDetailSerializer
    queryset = Charm.objects.all()
    permission_classes = [IsBotAuthenticated]


class AdminContactViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContactListSerializer
    detail_serializer_class = ContactDetailSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAdminAuthenticated]


class ContactViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContactListSerializer
    detail_serializer_class = ContactDetailSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsBotAuthenticated]


class AdminFavoriteViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = FavoriteListSerializer
    detail_serializer_class = FavoriteDetailSerializer
    queryset = Favorite.objects.all()
    permission_classes = [IsAdminAuthenticated]


class FavoriteViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = FavoriteListSerializer
    detail_serializer_class = FavoriteDetailSerializer
    queryset = Favorite.objects.all()
    permission_classes = [IsBotAuthenticated]


class AdminDistanceViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = DistanceListSerializer
    detail_serializer_class = DistanceDetailSerializer
    queryset = Distance.objects.all()
    permission_classes = [IsAdminAuthenticated]

class DistanceViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = DistanceListSerializer
    detail_serializer_class = DistanceDetailSerializer
    queryset = Distance.objects.all()
    permission_classes = [IsBotAuthenticated]


class AdminKeywordViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = KeywordListSerializer
    detail_serializer_class = KeywordDetailSerializer
    queryset = Keyword.objects.all()
    permission_classes = [IsAdminAuthenticated]


class KeywordViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = KeywordListSerializer
    detail_serializer_class = KeywordDetailSerializer
    queryset = Keyword.objects.all()
    permission_classes = [IsBotAuthenticated]