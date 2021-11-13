"""
Serializer for Profiles App
"""
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """ Comment serializer """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    name = serializers.ReadOnlyField(source='owner.profile.name')
    position = serializers.ReadOnlyField(source='owner.profile.position')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Meta for Comments Serializer """
        model = Comment()
        fields = [
            'id', 'owner', 'post', 'created_at', 'updated_at', 'content',
            'is_owner', 'profile_id', 'name', 'position', 'profile_image',
        ]
