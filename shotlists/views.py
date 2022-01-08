""" Views for Shotlist App """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Shotlist
from .serializers import ShotlistSerializer


class ShotlistList(generics.ListCreateAPIView):
    """ List all Shotlists """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ShotlistSerializer
    queryset = Shotlist.objects.all().order_by('scene_number', 'shot_number')

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['scene_id', 'scene_number', 'shot_number']

    search_fields = [
            'scene_number',
            'shot_number',
            ]


class ShotlistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete Shotlist
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ShotlistSerializer
    queryset = Shotlist.objects.all()
