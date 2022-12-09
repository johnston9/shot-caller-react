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
            'id', 'day', 'date',
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
            'scene_id', 'id', 'day_id', 'day', 'day_order_number',
            'date', 'number', 'title', 'start_time', 'end_time',
            'int_ext', 'time', 'action', 'act', 'day_night',
            'dramatic_day', 'location', 'pages',
            'location_detail', 'filming_location', 'location_address',
            'equip_set_props', 'department_info', 'next', 'new_info',
            ]
