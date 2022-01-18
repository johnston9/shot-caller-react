""" Generic Locations views """
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import Location
from .serializers import LocationSerializer


class LocationList(generics.ListCreateAPIView):
    """
    List Location or create a Location if logged in.
    """
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Location.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        ]

    filterset_fields = ['name']

    search_fields = ['name']


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a Location, or update or delete it by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
