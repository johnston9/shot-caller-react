""" Views for Scenes App """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_react.permissions import IsOwnerOrReadOnly
from .models import Scene
from .serializers import SceneSerializer


class ScenesList(generics.ListCreateAPIView):
    """ List all Scenes """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SceneSerializer
    queryset = Scene.objects.all().order_by('number')

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['act', 'location']

    search_fields = ['number', 'location', 'title']

    ordering_fields = [
        'location',
        'number',
    ]


class SceneDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get and put Scene
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SceneSerializer
    queryset = Scene.objects.all()
