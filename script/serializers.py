"""
Serializer for Script App
"""
from rest_framework import serializers
from .models import Script


class ScriptSerializer(serializers.ModelSerializer):
    """
    Serializer class for Script App
    """

    class Meta:
        """
        Meta for Script Serializer
        """
        model = Script
        fields = [
            'id', 'draft', 'created_at', 'updated_at', 'latest_changes',
            'notes', 'script',
        ]
