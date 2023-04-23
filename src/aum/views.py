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

    serializer_class = VisitListSerializer
    detail_serializer_class = VisitDetailSerializer
    queryset = Ban.objects.all()
    permission_classes = [IsAdminAuthenticated]

class BanViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = VisitListSerializer
    detail_serializer_class = VisitDetailSerializer
    queryset = Ban.objects.all()
    permission_classes = [IsBotAuthenticated]