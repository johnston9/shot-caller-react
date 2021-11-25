""" Views for Scenes App """
from rest_framework import generics, permissions
from shot_caller_react.permissions import IsOwnerOrReadOnly
from .models import Scene
from .serializers import SceneSerializer

class ScenesList(generics.ListCreateAPIView):
    """ List all Scenes """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SceneSerializer
    queryset = Scene.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SceneDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get and put Scene
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SceneSerializer
    queryset = Scene.objects.all()
