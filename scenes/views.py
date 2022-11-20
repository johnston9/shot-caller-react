""" Views for the Scenes App """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_react.permissions import IsOwnerOrReadOnly
from .models import Scene
from .serializers import SceneSerializer
from .models import SceneCharacterAdd
from .serializers import SceneCharacterAddSerializer
from .models import SceneBGAdd
from .serializers import SceneBGAddSerializer


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


class SceneCharacterAddList(generics.ListCreateAPIView):
    """ List all SceneCharacterAdds """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SceneCharacterAddSerializer
    queryset = SceneCharacterAdd.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['scene_id', 'role']

    search_fields = ['role']


class SceneCharacterAddDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete SceneCharacterAdds
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SceneCharacterAddSerializer
    queryset = SceneCharacterAdd.objects.all()


class SceneBGAddList(generics.ListCreateAPIView):
    """ List all SceneBGAdds """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SceneBGAddSerializer
    queryset = SceneBGAdd.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['scene_id', 'role']

    search_fields = ['role']


class SceneBGAddDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete SceneBGAdd
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SceneBGAddSerializer
    queryset = SceneBGAdd.objects.all()
