""" Views for Callsheet App """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import CrewInfonew
from .serializers import CrewInfonewSerializer
from .models import Callsheetnew
from .serializers import CallsheetnewSerializer
from .models import Castcallnew
from .serializers import CastcallnewSerializer
from .models import Backgroundcallnew
from .serializers import BackgroundcallnewSerializer


class CrewInfonewList(generics.ListCreateAPIView):
    """ List all Crew info """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CrewInfonewSerializer
    queryset = CrewInfonew.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['production_name']

    search_fields = ['production_name']


class CrewInfonewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete CrewInfo
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CrewInfonewSerializer
    queryset = CrewInfonew.objects.all()


class CallsheetnewList(generics.ListCreateAPIView):
    """ List all Callsheets """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CallsheetnewSerializer
    queryset = Callsheetnew.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['day', 'date']

    search_fields = ['day', 'date']


class CallsheetnewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete Callsheet
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CrewInfonewSerializer
    queryset = Callsheetnew.objects.all()


class CastcallnewList(generics.ListCreateAPIView):
    """ List all Castcalls """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CastcallnewSerializer
    queryset = Castcallnew.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['day_id', 'role']

    search_fields = ['day', 'date', 'role']


class CastcallnewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete Castcalls
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CastcallnewSerializer
    queryset = Castcallnew.objects.all()


class BackgroundcallnewList(generics.ListCreateAPIView):
    """ List all Backgroundcalls """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BackgroundcallnewSerializer
    queryset = Backgroundcallnew.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
        ]

    filterset_fields = ['day_id', 'type']

    search_fields = ['day', 'date', 'type']


class BackgroundcallnewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put and delete Backgroundcalls
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BackgroundcallnewSerializer
    queryset = Backgroundcallnew.objects.all()
