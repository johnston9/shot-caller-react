"""
Serializer for Scenes App
"""
from rest_framework import serializers
from .models import Scene
from .models import SceneCharacterAdd
from .models import SceneBGAdd


class SceneSerializer(serializers.ModelSerializer):
    """
    Serializer class for Scene App
    """

    class Meta:
        """
        Meta for Scene Serializer
        """
        model = Scene
        fields = '__all__'
        # fields = [
        #     'id', 'number', 'act', 'created_at', 'updated_at', 'title',
        #     'int_ext', 'day_night', 'time', 'location', 'filming_location',
        #     'action', 'equip_set_props', 'dramatic_day', 'department_info',
        #     'script', 'character1', 'shooting_date', storyboard_url,
        #     'workspace_guide', 'storyboard', 'pages', 'location_detail',
        # ]


class SceneCharacterAddSerializer(serializers.ModelSerializer):
    """
    Serializer class for the SceneCharacterAdd model
    """

    class Meta:
        """
        Meta for SceneCharacterAdd Serializer
        """
        model = SceneCharacterAdd
        fields = '__all__'


class SceneBGAddSerializer(serializers.ModelSerializer):
    """
    Serializer class for the SceneBGAdd model
    """

    class Meta:
        """
        Meta for SceneBGAdd Serializer
        """
        model = SceneBGAdd
        fields = '__all__'
