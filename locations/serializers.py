""" Locations serializer """
from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    """ Locations serializer """

    class Meta:
        model = Location
        fields = [
            'id', 'name', 'description', 'filming_address_primary',
            'filming_address2', 'filming_address3',
            'image1_description', 'image1', 'image2_description', 'image2',
            'image3_description', 'image3', 'image4_description', 'image4',
            'image5_description', 'image5', 'image6_description', 'image6',
            'image7_description', 'image7', 'image8_description', 'image8',
        ]
