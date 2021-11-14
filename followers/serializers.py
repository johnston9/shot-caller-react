""" serializer for Follower model """
from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """ Follower serializers """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_username = serializers.ReadOnlyField(source='followed.username')
    followed_name = serializers.ReadOnlyField(source='followed.profile.name')
    followed_position = serializers.ReadOnlyField(source='followed.profile.position')

    class Meta:
        """ Meta for Follower Serializer """
        model = Follower
        fields = ['id', 'created_at', 'owner', 'followed',
        'followed_name', 'followed_username', 'followed_position',]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
