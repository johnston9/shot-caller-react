""" Views for Profiles App """
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from shot_caller_react.permissions import IsOwnerOrReadOnly


class ProfileList(APIView):
    """ List all profiles, profile creation handled by django signals """
    def get(self, request):
        """ View """
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)


class ProfileDetail(APIView):
    """ Get and put profile """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """ View """
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """ View """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        """ View """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
