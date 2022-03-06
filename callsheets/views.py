""" Views for Callsheet App """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import CrewInfo
from .serializers import CrewInfoSerializer


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
