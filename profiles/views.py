""" GENERICS VIEWS for the profiles app """
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_react.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
        'name',
        'owner',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

    search_fields = ['name', 'owner']


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer


# """ Views for Profiles App """
# from django.db.models import Count
# from django.http import Http404
# from rest_framework import status, filters
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Profile
# from .serializers import ProfileSerializer
# from shot_caller_react.permissions import IsOwnerOrReadOnly


# class ProfileList(APIView):
#     """ List all profiles, profile creation handled by django signals """
#     def get(self, request):
#         """ View """
#         profiles = Profile.objects.all()
    #       queryset = Profile.objects.annotate(
    #     posts_count=Count('owner__post', distinct=True),
    #     followers_count=Count('owner__followed', distinct=True),
    #     following_count=Count('owner__following', distinct=True)
    # ).order_by('-created_at')
#         serializer = ProfileSerializer(profiles, many=True, context={'request': request})
#         return Response(serializer.data)


# class ProfileDetail(APIView):
#     """ Get and put profile """
#     serializer_class = ProfileSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         """ View """
#         try:
#             profile = Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         """ View """
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, pk):
#         """ View """
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
