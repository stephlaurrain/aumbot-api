from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from aum.views import VisitViewset, AdminVisitViewset


router = routers.SimpleRouter()
router.register('visit', VisitViewset, basename='visit')
router.register('admin/visit', AdminVisitViewset, basename='admin-visit')
router.register('ban', VisitViewset, basename='ban')
router.register('admin/ban', AdminVisitViewset, basename='admin-ban')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/', include(router.urls))
]
