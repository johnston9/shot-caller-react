"""
Serializer for Scenes App
"""
from rest_framework import serializers
from .models import Scene


class SceneSerializer(serializers.ModelSerializer):
    """
    Serializer class for Scene App
    """
    shooting_date = serializers.DateField(
        format="%d %b %Y", input_formats=['%d %b %Y'])

    class Meta:
        """
        Meta for Scene Serializer
        """
        model = Scene
        fields = [
            'id', 'number', 'act', 'created_at', 'updated_at', 'title',
            'int_ext', 'day_night', 'time', 'location', 'filming_location',
            'action', 'content', 'shotlist', 'storyboard', 'info', 'image',
            'character1', 'character1_costume', 'character2',
            'character2_costume', 'character3', 'character3_costume',
            'character4', 'character4_costume', 'character5',
            'character5_costume', 'character6', 'character6_costume',
            'character7', 'character7_costume', 'character8',
            'character8_costume', 'character9', 'character9_costume',
            'character10', 'character10_costume', 'background_artists',
            'background_artists_costumes', 'other_characters',
            'other_characters_costumes', 'shooting_date',
        ]
