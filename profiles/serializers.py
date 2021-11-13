"""
Serializer for Profiles App
"""
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer class for Profiles App """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Meta for Profiles Serializer """
        model = Profile
        fields = [
            'id', 'owner', 'position', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner'
        ]
