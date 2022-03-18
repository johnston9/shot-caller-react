"""
Serializer for Callsheetnew App
"""
from rest_framework import serializers
from .models import CrewInfonew
from .models import Callsheetnew
from .models import Castcallnew
from .models import Backgroundcallnew


class CrewInfonewSerializer(serializers.ModelSerializer):
    """
    Serializer class for the CrewInfonew model
    """

    class Meta:
        """
        Meta for CrewInfonew Serializer
        """
        model = CrewInfonew
        fields = '__all__'


class CallsheetnewSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Callsheetnew model
    """

    class Meta:
        """
        Meta for Callsheetnew Serializer
        """
        model = Callsheetnew
        fields = '__all__'


class CastcallnewSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Castcallnew model
    """

    class Meta:
        """
        Meta for Castcallnew Serializer
        """
        model = Castcallnew
        fields = '__all__'


class BackgroundcallnewSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Backgroundcallnew model
    """

    class Meta:
        """
        Meta for Backgroundcallnew Serializer
        """
        model = Backgroundcallnew
        fields = '__all__'
