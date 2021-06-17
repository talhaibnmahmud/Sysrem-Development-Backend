from django.urls import path, include
from rest_framework import routers

from .views import RentalListView, DivisionViewSet, DistrictViewSet

router = routers.DefaultRouter()
router.register('division', DivisionViewSet)
router.register('district', DistrictViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all/', RentalListView.as_view(), name="Rental-List-View"),
]
