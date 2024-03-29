""" serializer for Archive model """
from django.db import IntegrityError
from rest_framework import serializers
from .models import Archive


class ArchiveSerializer(serializers.ModelSerializer):
    """ Archive serializers """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """ Meta for Archive Serializer """
        model = Archive
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
