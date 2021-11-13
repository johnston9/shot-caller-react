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
            'id', 'number', 'created_at', 'updated_at', 'title', 'int_ext',
            'time', 'location', 'characters', 'action', 'content','shotlist',
            'storyboard', 'info', 'image'
        ]
