from django.urls import include,path
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register(r'personnes',personViewSet)
router.register(r'taximans',taximanViewSet)
router.register(r'declarationDePertes',declarationDePerteViewSet)
router.register(r'objetperdus',objetPerduViewSet)
router.register(r'passagers',passagerViewSet)
router.register(r'adminstrateurs',administrateurViewSet)
router.register(r'reservations',reservationViewSet)
router.register(r'messages',messageViewSet)

urlpatterns=[path('',include(router.urls)),]