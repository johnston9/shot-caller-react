""" IndexShot1 serializers """
from rest_framework import serializers
from .models import IndexShot
from .models import Series


class SeriesSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Series model
    """

    class Meta:
        """
        Meta for Series Serializer
        """
        model = Series
        fields = [
            'id', 'name', 'content']


class IndexShotSerializer(serializers.ModelSerializer):
    """ IndexShot serializer """

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
        model = IndexShot
        fields = [
            'series_id', 'series_name', 'number',
            'id', 'content', 'image']
