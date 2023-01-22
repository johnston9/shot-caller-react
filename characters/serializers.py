""" Characters serializer """
from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    """ Characters serializer
        'project_name', 'project_id', 'project_stripe_id', """

    class Meta:
        model = Character
        fields = [
            'number', 'id', 'role', 'actor', 'pickup_address',
            'pickup_address_2', 'make_up_time', 'commute_time',
            'email', 'mobile', 'agent', 'diet', 'requirements', 'costume1',
            'costume2', 'costume3', 'costume4', 'makeup', 'username',
            'costume5', 'costume6', 'costume7', 'costume1_image',
            'costume2_image', 'costume3_image', 'costume4_image',
            'costume5_image', 'costume6_image', 'costume7_image',
            'makeup_image',
        ]
