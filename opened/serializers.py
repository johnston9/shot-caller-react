""" serializer for Opened model """
from django.db import IntegrityError
from rest_framework import serializers
from .models import Opened


class OpenedSerializer(serializers.ModelSerializer):
    """ Opened serializers """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """ Meta for Opened Serializer """
        model = Opened
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
