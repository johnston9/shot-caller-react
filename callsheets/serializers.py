"""
Serializer for Callsheet App
"""
from rest_framework import serializers
from .models import CrewInfo


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
