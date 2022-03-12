"""
Serializer for Schedule App
"""
from rest_framework import serializers
from .models import Day
from .models import ScheduleScene
# from django.contrib.humanize.templatetags.humanize import naturaltime


class DaySerializer(serializers.ModelSerializer):
    """
    Serializer class for Schedule App Day model
    """
    date = serializers.DateField(format="%d %b %Y", input_formats=['%d %b %Y'])

    class Meta:
        """
        Meta for Day Serializer
        """
        model = Day
        fields = [
            'id', 'day', 'date', 'scene1', 'scene2', 'scene3', 'scene4',
            'scene5', 'scene6', 'scene7', 'scene8', 'scene9', 'scene10',
            'scene11', 'scene12', 'location1', 'xtra_scenes', 'crewcall',
            ]


class ScheduleSceneSerializer(serializers.ModelSerializer):
    """
    Serializer class for Schedule App ScheduleScene model
    """

    class Meta:
        """
        Meta for ScheduleScene Serializer
        """
        model = ScheduleScene
        fields = [
            'id', 'day_id', 'day', 'day_order_number', 'date', 'number',
            'title', 'start_time', 'end_time', 'content', 'location',
            'filming_location', 'int_ext', 'time', 'location_address',
            'action', 'info', 'act', 'new_content', 'new_info', 'day_night',
            'character1', 'character1_costume', 'character2', 'pages',
            'character2_costume', 'character3', 'character3_costume',
            'character4', 'character4_costume', 'character5',
            'character5_costume', 'character6', 'character6_costume',
            'character7', 'character7_costume', 'character8',
            'character8_costume', 'character9', 'character9_costume',
            'character10', 'character10_costume',
            'character11', 'character11_costume',
            'character12', 'character12_costume', 'other_characters',
            'other_characters_costumes', 'background_artists',
            'background_artists_costumes',
            'character1_number', 'character2_number',
            'character3_number', 'character4_number',
            'character5_number', 'character6_number',
            'character7_number', 'character8_number',
            'character9_number', 'character10_number',
            'character11_number', 'character12_number',
            'other_characters_numbers',
            ]
