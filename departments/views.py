""" Generics views for the Department app """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_react.permissions import IsOwnerOrReadOnly
from .models import Department
from .serializers import DepartmentSerializer


class DepartmentList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Department.objects.all().order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'departments',
    ]
    search_fields = [
        'owner__profile__name',
        'title',
    ]
    ordering_fields = [
        'created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Department.objects.all()
