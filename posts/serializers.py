""" Posts serializer """
from rest_framework import serializers
from likes.models import Like
from archives.models import Archive
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """ Posts serializer """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    name = serializers.ReadOnlyField(source='owner.profile.name')
    position = serializers.ReadOnlyField(source='owner.profile.position')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    archive_id = serializers.SerializerMethodField()

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

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            print(like)
            return like.id if like else None
        return None

    def get_archive_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            archive = Archive.objects.filter(
                owner=user, post=obj
            ).first()
            print(archive)
            return archive.id if archive else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'scene', 'number', 'departments', 'category',
            'created_at', 'updated_at', 'title', 'like_id',
            'content', 'is_owner', 'profile_id', 'archive_id',
            'name', 'position', 'profile_image',
            'image1', 'image2', 'image3', 'image4', 'image5',
            'comments_count', 'likes_count',
        ]
