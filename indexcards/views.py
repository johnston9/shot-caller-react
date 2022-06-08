""" Generic IndexCard views """
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import IndexCard
from .serializers import IndexCardSerializer


class IndexCardList(generics.ListCreateAPIView):
    """
    List IndexCard or create a IndexCard if logged in.
    """
    serializer_class = IndexCardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = IndexCard.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        ]

    filterset_fields = ['number']

    search_fields = ['number']


class IndexCardDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an IndexCard, or update or delete it by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = IndexCardSerializer
    queryset = IndexCard.objects.all()
