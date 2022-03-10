"""
Serializer for Callsheet App
"""
from rest_framework import serializers
from .models import CrewInfo
from .models import Callsheet
from .models import Castcall


class CrewInfoSerializer(serializers.ModelSerializer):
    """
    Serializer class for the CrewInfo model
    """

    class Meta:
        """
        Meta for CrewInfo Serializer
        """
        model = CrewInfo
        fields = '__all__'


class CallsheetSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Callsheet model
    """

    class Meta:
        """
        Meta for Callsheet Serializer
        """
        model = Callsheet
        fields = '__all__'


class CastcallSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Castcall model
    """

    class Meta:
        """
        Meta for Castcall Serializer
        """
        model = Castcall
        fields = '__all__'
