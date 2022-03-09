""" Views for Callsheet App """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import CrewInfo
from .serializers import CrewInfoSerializer
from .models import Callsheet
from .serializers import CallsheetSerializer


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
