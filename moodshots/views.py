""" Generics views for the Moodshots app 
    In Shot Caller DRF the work Mootshot is used throughout
    for the Moodboard App in Shot Caller React
"""
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Moodshot
from .serializers import MoodshotSerializer


class MoodshotList(generics.ListCreateAPIView):
    """
    List Moodshots or create a Moodshot if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = MoodshotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Moodshot.objects.all().order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'scene',
        'number',
        'character',
        'location',
    ]
    search_fields = [
        'number',
        'character',
        'location',
    ]
    ordering_fields = [
        'number',
        'character',
        'location',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MoodshotDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a Moodshot and edit or delete it if you own it.
    """
    serializer_class = MoodshotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Moodshot.objects.all()
