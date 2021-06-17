from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework import viewsets

from rental.models import Division, District
from rental.serializers import AreaSerializer, DistrictSerializer


# Create your views here.
class RentalListView(ListView):

    def get(self, request, **kwargs):
        items = {}

        divisions = Division.objects.all()
        districts = District.objects.all()

        for division in divisions:
            district = districts.filter(division=division)
            dis = [(i.name, i.id) for i in district]
            items[division.name] = dis

        return JsonResponse(items)


class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = AreaSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
