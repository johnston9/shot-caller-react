"""
Serializer for Shotlists App
"""
from rest_framework import serializers
from .models import Shotlist


class ShotlistSerializer(serializers.ModelSerializer):
    """
    Serializer class for Schedule App Shotlist model
    """

    class Meta:
        """
        Meta for Shotlist Serializer
        """
        model = Shotlist
        fields = [
            'id', 'scene_id', 'scene_number', 'shot_number', 'size', 'angle',
            'movement', 'fx', 'description', 'storyboard_refs', 'focus_pulls',
            'lens', 'equipment', 'lighting', 'audio', 'camera', 'script_ref',
            'audio', 'image', 'framing', 'int_ext', 'frame_rate', 'location',
            'actors', 'notes', 'day_night',
            ]
