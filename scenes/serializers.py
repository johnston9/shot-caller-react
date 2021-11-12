"""
Serializer for Scenes App
"""
from rest_framework import serializers
from .models import Scene


class SceneSerializer(serializers.ModelSerializer):
    """
    Serializer class for Scene App
    """

    class Meta:
        """
        Meta for Scene Serializer
        """
        model = Scene
        fields = [
            'id', 'number', 'title', 'created_at', 'updated_at', 'int_ext',
            'content', 'image', 'info', 'time', 'location', 'action',
            'characters', 
        ]
