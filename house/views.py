from django.http import JsonResponse
from django.views.generic import DetailView
from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets, status
from rest_framework.response import Response

from house.models import House
from house.serializers import HouseSerializer
from rental.models import District, Division


# Create your views here.


class HouseViewSet(viewsets.ModelViewSet):
    queryset            = House.objects.all()
    serializer_class    = HouseSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly, ]
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter, ]
    filterset_fields    = '__all__'
    search_fields       = ['title', 'address', 'description', ]

    def perform_create(self, serializer):
        division = Division.objects.get(pk=self.request.data['division'])
        district = District.objects.get(pk=self.request.data['district'])
        serializer.save(
            owner=self.request.user,
            division=division,
            district=district)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         house = serializer.data
    #         house.owner = request.user
    #         self.perform_create(house)
    #         headers = self.get_success_headers(house)
    #         return Response(house, status=status.HTTP_201_CREATED, headers=headers)
