""" Generic IndexCard views """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import IndexCard
from .serializers import IndexCardSerializer


class IndexCardList(generics.ListCreateAPIView):
    """
    List IndexCard or create a IndexCard if logged in.
    """
    serializer_class = IndexCardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = IndexCard.objects.all().order_by('number')

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['number']

    search_fields = ['number']

    ordering_fields = [
        'number',
    ]


class IndexCardDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an IndexCard, or update or delete it by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = IndexCardSerializer
    queryset = IndexCard.objects.all()
