from rest_framework import serializers

from house.models import House
from rental.models import District, Division


class HouseSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField()
    division = serializers.StringRelatedField()

    class Meta:
        model   = House
        exclude = [
            'owner',
            'last_modified',
        ]

    # def create(self, validated_data):
    #     house = House(validated_data)
    #     house.owner = request.data
    # district = House.district.name
