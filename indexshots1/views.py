""" Generic IndexShot1 views """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Series
from .serializers import SeriesSerializer
from .models import IndexShot
from .serializers import IndexShotSerializer


class SeriesList(generics.ListCreateAPIView):
    """ List all Series """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SeriesSerializer
    queryset = Series.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['name', ]

    search_fields = ['name']


class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete Series
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SeriesSerializer
    queryset = Series.objects.all()


class IndexShotList(generics.ListCreateAPIView):
    """
    List IndexShot or create a IndexShot if logged in.
    """
    serializer_class = IndexShotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = IndexShot.objects.all().order_by('number')

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = [
        'number',
        'series_id',
    ]

    search_fields = [
        'number',
    ]

    ordering_fields = [
        'number',
    ]


class IndexShotDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an IndexShot, or update or delete it by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = IndexShotSerializer
    queryset = IndexShot.objects.all()
