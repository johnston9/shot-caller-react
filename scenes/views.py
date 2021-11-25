""" Views for Scenes App """
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import Scene
from .serializers import SceneSerializer


class ScenesList(APIView):
    """ List all Scenes """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        """ View to get all scenes """
        scenes = Scene.objects.all()
        serializer = SceneSerializer(
            scenes, many=True, context={'request': request})
        return Response(serializer.data)


class SceneDetail(APIView):
    """ Get and put Scene """
    serializer_class = SceneSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """ View to get a scene"""
        try:
            scene = Scene.objects.get(pk=pk)
            return scene
        except Scene.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """ View """
        scene = self.get_object(pk)
        serializer = SceneSerializer(scene, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        """ View """
        scene = self.get_object(pk)
        serializer = SceneSerializer(
            scene, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
