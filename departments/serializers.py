""" Departments serializer """
from rest_framework import serializers
from .models import Department
from opened.models import OpenedDept


class DepartmentSerializer(serializers.ModelSerializer):
    """ Department serializer """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    name = serializers.ReadOnlyField(source='owner.profile.name')
    position = serializers.ReadOnlyField(source='owner.profile.position')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    opened_id = serializers.SerializerMethodField()

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

    def get_opened_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            opened = OpenedDept.objects.filter(
                owner=user, post=obj
            ).first()
            print(opened)
            return opened.id if opened else None
        return None

    class Meta:
        model = Department
        fields = [
            'id', 'owner', 'departments', 'created_at', 'updated_at',
            'title', 'content', 'is_owner', 'profile_id', 'name',
            'position', 'profile_image', 'image1', 'image2', 'image3',
            'image4', 'image5', 'opened_id',
        ]
