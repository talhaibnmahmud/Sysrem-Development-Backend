from django.urls import include, path
from rest_framework import routers

from house.views import HouseViewSet

router = routers.DefaultRouter()
router.register('', HouseViewSet)

urlpatterns = [
    path('', include(router.urls), name='house-list'),
]
