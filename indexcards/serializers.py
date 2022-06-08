""" IndexCard serializer """
from rest_framework import serializers
from .models import IndexCard


class IndexCardSerializer(serializers.ModelSerializer):
    """ IndexCard serializer """

    class Meta:
        model = IndexCard
        fields = [
            'number', 'id', 'story', 'style', ]
