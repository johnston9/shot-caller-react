""" Views for Callsheet App """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import CrewInfo
from .serializers import CrewInfoSerializer
from .models import Callsheet
from .serializers import CallsheetSerializer
from .models import Castcall
from .serializers import CastcallSerializer


class CrewInfoList(generics.ListCreateAPIView):
    """ List all Crew info """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CrewInfoSerializer
    queryset = CrewInfo.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['production_name']

    search_fields = ['production_name']


class CrewInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete CrewInfo
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CrewInfoSerializer
    queryset = CrewInfo.objects.all()


class CallsheetList(generics.ListCreateAPIView):
    """ List all Callsheets """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CallsheetSerializer
    queryset = Callsheet.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['day', 'date']

    search_fields = ['day', 'date']


class CallsheetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete Callsheet
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CrewInfoSerializer
    queryset = Callsheet.objects.all()


class CastcallList(generics.ListCreateAPIView):
    """ List all Castcalls """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CastcallSerializer
    queryset = Castcall.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['day_id', 'role']

    search_fields = ['day', 'date', 'role']


class CastcallDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete Castcalls
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CastcallSerializer
    queryset = Castcall.objects.all()
