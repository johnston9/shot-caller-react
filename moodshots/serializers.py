""" Moodshots serializer """
from rest_framework import serializers
from .models import Moodshot


class MoodshotSerializer(serializers.ModelSerializer):
    """ Moodshots serializer """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    name = serializers.ReadOnlyField(source='owner.profile.name')
    position = serializers.ReadOnlyField(source='owner.profile.position')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Moodshot
        fields = [
            'id', 'owner', 'scene', 'number', 'created_at', 'updated_at',
            'title', 'content', 'character', 'location',
            'image1', 'image2', 'image3', 'image4', 'image5',
            'is_owner', 'profile_id', 'name', 'position', 'profile_image',
        ]
