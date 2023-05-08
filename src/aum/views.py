import logging

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from aum.permissions import IsAdminAuthenticated, IsBotAuthenticated
from aum.models.visit import Visit

#import json
from datetime import datetime
#ici ajoute modeles pour migration

from aum.models.visit import Visit
from aum.models.ban import Ban
from aum.models.charm import Charm
from aum.models.contact import Contact
from aum.models.distance import Distance
from aum.models.favorite import Favorite
from aum.models.keyword import Keyword
from aum.models.stat import Stat

from aum.serializers.visit import VisitDetailSerializer, VisitListSerializer
from aum.serializers.ban import BanDetailSerializer, BanListSerializer
from aum.serializers.charm import CharmDetailSerializer, CharmListSerializer
from aum.serializers.contact import ContactDetailSerializer, ContactListSerializer
from aum.serializers.distance import DistanceDetailSerializer, DistanceListSerializer
from aum.serializers.favorite import FavoriteDetailSerializer, FavoriteListSerializer
from aum.serializers.keyword import KeywordDetailSerializer, KeywordListSerializer
from aum.serializers.stat import StatDetailSerializer, StatListSerializer

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
    queryset = Visit.objects.all().order_by('score').values()
    permission_classes = [IsBotAuthenticated]
    paginator = None

    @action(detail=False, methods=['post'])
    def clean(self, request):        
        Visit.objects.all().delete()
        return Response()  

    @action(detail=False)
    def count(self, request):        
        res = Visit.objects.count()
        return Response(data={"count":res})

    @action(detail=False)
    def dumb(self, request):        
        # print(str(request.query_params))
        threshold = request.query_params['threshold']
        res = Visit.objects.filter(score__gt=threshold).count()  # (gte)                
        return Response(data={"count":res})

    @action(detail=False, methods=['patch'])
    def datevisit(self, request):        
        # print(request.data['aum_id'])
        aum_id = request.data['aum_id']
        Visit.objects.filter(aum_id=aum_id).update(date_visit=datetime.now()) 
        return Response()

    @action(detail=False)
    def isin(self, request):        
        aum_id = request.query_params['aum_id']
        res = Visit.objects.filter(aum_id=aum_id).first()        
        return Response(data={"isin":res is not None})

    @action(detail=False)
    def isinrecently(self, request):        
        aum_id = request.query_params['aum_id']
        datemax = request.query_params['datemax']
        res = Visit.objects.filter(aum_id=aum_id, date_visit__gt=datemax).first()        
        return Response(data={"isin": res is not None})

    @action(detail=False)
    def test(self, request):        
        print(str(request.query_params))
        return Response(data={"prout": "prout"})

    @action(detail=False)
    def linebyaumid(self, request):        
        aum_id = request.query_params['aum_id']
        res = Visit.objects.filter(aum_id=aum_id).values().first()
        return Response(data={"line": res})
    
    @action(detail=False)
    def listwithdelay(self, request):        
        datemax = request.query_params['datemax']
        res = Visit.objects.filter(date_visit__lt=datemax).order_by('score').values()
        return Response(res)
        
    @action(detail=False)
    def listhot(self, request):        
        datemax = request.query_params['datemax']
        threshold = request.query_params['threshold']
        # res = Visit.objects.filter(score__lte=threshold, date_visit__gte=datemax).order_by('date_visit', 'score').values()        
        res = Visit.objects.filter(hot__gte=threshold, date_visit__gte=datemax).order_by('date_visit', 'score').values()        
        # return self.session.query(visit).filter(and_(visit.score<=seuil, visit.date_visit>=datemax)).order_by(visit.date_visit, visit.score).all()
        return Response(res)
                
    @action(detail=False)
    def listdumb(self, request):        
        threshold = request.query_params['threshold']
        res = Visit.objects.filter(score__lte=threshold).values()        
        # return self.session.query(visit).filter(visit.score>=seuil).all()
        return Response(res)

    @action(detail=False)
    def stat(self, request):        
        from django.db.models import Count, Case, When, Value, CharField, Q
        from django.db.models.functions import Cast, Extract, TruncDate, ExtractMonth, ExtractWeekDay, Extract
        from datetime import datetime
        # a marche po

        my_case_stmt = Case(         
            When(date_first_visit__week_day=1, then=Value("sunday")), 
            When(date_first_visit__week_day=2, then=Value("monday")),
            When(date_first_visit__week_day=3, then=Value("tuesday")),
            When(date_first_visit__week_day=4, then=Value("wednesday")),
            When(date_first_visit__week_day=5, then=Value("thursday")),
            When(date_first_visit__week_day=6, then=Value("friday")),
            When(date_first_visit__week_day=7, then=Value("saturday")),          
            default=Value("noday"),
            output_field=CharField()
        )
        res = Visit.objects.exclude(date_first_visit__isnull=True).annotate(
            day=my_case_stmt,
            date=TruncDate('date_first_visit')
                ).values('day', 'date').annotate(
                            count=Count('id')
                ).order_by('date').all()
        print(res)
        # return Response(res)
        return Response(res)
           

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
    paginator = None

    # @action(detail=True, methods=['post'])
    # def delete(self, request, pk):        
    #     Ban.objects.filter(aum_id=pk).delete()
    #     return Response()
    
    @action(detail=False, methods=['post'])
    def delete(self, request):        
        print(request.data['aum_id'])
        Ban.objects.filter(aum_id=request.data['aum_id']).delete()        
        return Response()

    @action(detail=False)
    def count(self, request):        
        res = Ban.objects.count()
        return Response(data={"count":res})

    @action(detail=False)
    def notdone(self, request):        
        res = Ban.objects.filter(done=False).values()
        return Response(res)

    @action(detail=False, methods=['patch'])
    def setdone(self, request):                
        aum_id = request.data['aum_id']
        done = request.data['done']
        Ban.objects.filter(aum_id=aum_id).update(done=done)
        return Response()

    @action(detail=False, methods=['put'])
    def reinitbanflag(self, request):                        
        Ban.objects.all().update(done=False)
        return Response()
    
    @action(detail=False)
    def isin(self, request):        
        aum_id = request.query_params['aum_id']
        res = Ban.objects.filter(aum_id=aum_id).first()        
        return Response(data={"isin":res is not None})

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
    paginator = None

    @action(detail=False, methods=['post'])
    def delete(self, request):        
        print(request.data['aum_id'])
        Charm.objects.filter(aum_id=request.data['aum_id']).delete()        
        return Response()
    
    @action(detail=False)
    def count(self, request):        
        res = Charm.objects.count()
        return Response(data={"count":res})
    
    @action(detail=False)
    def isin(self, request):        
        aum_id = request.query_params['aum_id']
        res = Charm.objects.filter(aum_id=aum_id).first()        
        return Response(data={"isin":res is not None})

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
    paginator = None

    @action(detail=False)
    def isin(self, request):        
        aum_id = request.query_params['aum_id']
        res = Contact.objects.filter(aum_id=aum_id).first()        
        return Response(data={"isin":res is not None})

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
    paginator = None

    @action(detail=False, methods=['post'])
    def clean(self, request):        
        Favorite.objects.all().delete()
        return Response()
    
    @action(detail=False, methods=['post'])
    def delete(self, request):        
        print(request.data['aum_id'])
        Favorite.objects.filter(aum_id=request.data['aum_id']).delete()        
        return Response()

    @action(detail=False)
    def isin(self, request):        
        aum_id = request.query_params['aum_id']
        res = Favorite.objects.filter(aum_id=aum_id).first()        
        return Response(data={"isin":res is not None})

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
    paginator = None

    @action(detail=False)
    def linebycity(self, request):        
        city = request.query_params['city']
        res = Distance.objects.filter(city=city).values().first()
        return Response(data={"line": res})


class AdminKeywordViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = KeywordListSerializer
    detail_serializer_class = KeywordDetailSerializer
    queryset = Keyword.objects.all()
    permission_classes = [IsAdminAuthenticated]


class KeywordViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = KeywordListSerializer
    detail_serializer_class = KeywordDetailSerializer
    queryset = Keyword.objects.all().order_by('word').values()
    permission_classes = [IsBotAuthenticated]
    paginator = None

    @action(detail=False)
    def isin(self, request):        
        word = request.query_params['word']
        res = Keyword.objects.filter(word=word).first()        
        return Response(data={"isin":res is not None})


class AdminStatViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = StatListSerializer
    detail_serializer_class = StatDetailSerializer
    queryset = Stat.objects.all()
    permission_classes = [IsAdminAuthenticated]


class StatViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = StatListSerializer
    detail_serializer_class = StatDetailSerializer
    queryset = Stat.objects.all().order_by('date_stat').values()
    permission_classes = [IsBotAuthenticated]
    paginator = None