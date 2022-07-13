from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from aum.permissions import IsAdminAuthenticated
from aum.models import Visit
from aum.serializers import VisitDetailSerializer, VisitListSerializer


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