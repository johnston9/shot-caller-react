""" IndexShot1 serializer """
from rest_framework import serializers
from .models import IndexShot1


class IndexShot1Serializer(serializers.ModelSerializer):
    """ IndexShot1 serializer """

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

    class Meta:
        model = IndexShot1
        fields = [
            'number', 'id', 'content', 'image', ]
