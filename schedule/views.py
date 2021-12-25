""" Views for Schedule App """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_react.permissions import IsOwnerOrReadOnly
from .models import Day
from .serializers import DaySerializer


class DayList(generics.ListCreateAPIView):
    """ List all Days """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DaySerializer
    queryset = Day.objects.all().order_by('day')

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['day', 'date']

    search_fields = [
            'scene1', 'scene2', 'scene3', 'scene4', 'scene5',
            'scene6', 'scene7', 'scene8', 'scene9', 'scene10', 'location1',
            'location2', 'location3', 'location4', 'location5',
            ]


class DayDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete Day
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DaySerializer
    queryset = Day.objects.all()
