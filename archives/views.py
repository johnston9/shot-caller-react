""" Archive views """
from rest_framework import generics, permissions
from shot_caller_react.permissions import IsOwnerOrReadOnly
from archives.models import Archive
from archives.serializers import ArchiveSerializer


class ArchiveList(generics.ListCreateAPIView):
    """
    List Archives or create a Archive if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ArchiveSerializer
    queryset = Archive.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArchiveDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an Archive or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ArchiveSerializer
    queryset = Archive.objects.all()
