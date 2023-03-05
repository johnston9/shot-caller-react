""" Opened views """
from rest_framework import generics, permissions
from shot_caller_react.permissions import IsOwnerOrReadOnly
from opened.models import Opened
from opened.serializers import OpenedSerializer
from opened.models import OpenedDept
from opened.serializers import OpenedDeptSerializer


class OpenedList(generics.ListCreateAPIView):
    """
    List Opened or create a Opened if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OpenedSerializer
    queryset = Opened.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OpenedDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an Opened or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = OpenedSerializer
    queryset = Opened.objects.all()


class OpenedDeptList(generics.ListCreateAPIView):
    """
    List OpenedDept or create a OpenedDept if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OpenedDeptSerializer
    queryset = OpenedDept.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OpenedDeptDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an OpenedDept or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = OpenedDeptSerializer
    queryset = OpenedDept.objects.all()
