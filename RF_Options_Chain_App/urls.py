from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UpdateDataView,ShowDataView

router = routers.DefaultRouter()
router.register('api_update', UpdateDataView)
router.register('opt_data', ShowDataView)


urlpatterns = [
    path('', include(router.urls)),
]