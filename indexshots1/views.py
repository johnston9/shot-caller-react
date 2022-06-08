""" Generic IndexShot1 views """
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import IndexShot1
from .serializers import IndexShot1Serializer


class IndexShot1List(generics.ListCreateAPIView):
    """
    List IndexShot1 or create a IndexShot1 if logged in.
    """
    serializer_class = IndexShot1Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = IndexShot1.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        ]

    filterset_fields = ['number']

    search_fields = ['number']


class IndexShot1Detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an IndexShot1, or update or delete it by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = IndexShot1Serializer
    queryset = IndexShot1.objects.all()
