"""
Serializer for Schedule App
"""
from rest_framework import serializers
from .models import Day
from django.contrib.humanize.templatetags.humanize import naturaltime


class DaySerializer(serializers.ModelSerializer):
    """
    Serializer class for Schedule App Day model
    """
    date = serializers.DateField(format="%d %b %Y", input_formats=['%d %b %Y'])
    # updated_at = serializers.SerializerMethodField()

    # def get_created_at(self, obj):
    #     return naturaltime(obj.created_at)

    class Meta:
        """
        Meta for Day Serializer
        """
        model = Day
        fields = [
            'day', 'date', 'scene1', 'scene2', 'scene3', 'scene4', 'scene5',
            'scene6', 'scene7', 'scene8', 'scene9', 'scene10', 'scene11',
            'scene12', 'location1', 'location2', 'location3', 'location4',
            'location5', 'location6',
            ]
