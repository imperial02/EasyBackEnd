from rest_framework import serializers
from restapi.models import Parking, Place, Section


class ParkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parking
        fields = ("id", "location", "name", "total_places")
        read_only_fields = ("total_places", "id", )


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ("id", "section", "place_status", "device_id")
        read_only_fields = ("id", )


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ("id", "parking", "name", "total_places")
        read_only_fields = ("total_places", "id", )
