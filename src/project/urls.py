from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from aum.views import VisitViewset, AdminVisitViewset, BanViewset, AdminBanViewset, CharmViewset, AdminCharmViewset, ContactViewset, AdminContactViewset, FavoriteViewset, AdminFavoriteViewset, DistanceViewset, AdminDistanceViewset, KeywordViewset, AdminKeywordViewset


router = routers.SimpleRouter()
router.register('visit', VisitViewset, basename='visit')
router.register('admin/visit', AdminVisitViewset, basename='admin-visit')
router.register('ban', BanViewset, basename='ban')
router.register('admin/ban', AdminBanViewset, basename='admin-ban')
router.register('charm', CharmViewset, basename='charm')
router.register('admin/charm', AdminCharmViewset, basename='admin-charm')
router.register('contact', ContactViewset, basename='contact')
router.register('admin/contact', AdminContactViewset, basename='admin-contact')
router.register('favorite', FavoriteViewset, basename='favorite')
router.register('admin/favorite', AdminFavoriteViewset, basename='admin-favorite')
router.register('distance', DistanceViewset, basename='distance')
router.register('admin/distance', AdminDistanceViewset, basename='admin-distance')
router.register('keyword', KeywordViewset, basename='keyword')
router.register('admin/keyword', AdminKeywordViewset, basename='admin-keyword')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/', include(router.urls))
]
