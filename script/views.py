""" Views for the Script App """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Script
from .serializers import ScriptSerializer


class ScriptList(generics.ListCreateAPIView):
    """ List all Scripts """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ScriptSerializer
    queryset = Script.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['draft']

    search_fields = ['draft']

    ordering_fields = [
        'created_at',
    ]


class ScriptDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get and put Script
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ScriptSerializer
    queryset = Script.objects.all()
