""" Generic Character views """
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import Character
from .serializers import CharacterSerializer


class CharacterList(generics.ListCreateAPIView):
    """
    List Character or create a Character if logged in.
    """
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Character.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        ]

    filterset_fields = ['role']

    search_fields = ['role']


class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a Character, or update or delete it by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
