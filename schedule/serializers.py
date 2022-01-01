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
            'scene11', 'scene12', 'location1', 'location2', 'location3',
            'location4', 'location5', 'location6', 'crewcall',
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
            'id', 'day_id', 'day', 'day_order_number', 'date', 'scene_number',
            'title', 'start_time', 'end_time', 'content', 'location',
            'filming_location', 'int_ext', 'day_night', 'time',
            'action', 'info', 'act', 'new_content', 'new_info',
            'character1', 'character1_costume', 'character2',
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
            'character1_calltime', 'character1_pickup',
            'character2_calltime', 'character2_pickup',
            'character3_calltime', 'character3_pickup',
            'character4_calltime', 'character4_pickup',
            'character5_calltime', 'character5_pickup',
            'character6_calltime', 'character6_pickup',
            'character7_calltime', 'character7_pickup',
            'character8_calltime', 'character8_pickup',
            'character9_calltime', 'character9_pickup',
            'character10_calltime', 'character10_pickup',
            'character11_calltime', 'character11_pickup',
            'character12_calltime', 'character12_pickup',
            'other_characters_calltimes', 'other_characters_pickups',
            'background_artists_calltimes', 'background_artists_costumes',
            ]
