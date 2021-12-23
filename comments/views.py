""" Generic comment views """
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from shot_caller_react.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'post',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()


# """ Comments views """
# from django.http import Http404
# from rest_framework import status, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from shot_caller_react.permissions import IsOwnerOrReadOnly
# from .models import Comment
# from .serializers import CommentSerializer, CommentDetailSerializer


# class CommentList(APIView):
#     """ Get Comments """
#     serializer_class = CommentSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def get(self, request):
#         """ Get Comments """
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(
#             comments, many=True, context={'request': request}
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         """ Create Comment """
#         serializer = CommentSerializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )


# class CommentDetail(APIView):
#     """ Get and put Comment """
#     serializer_class = CommentDetailSerializer
#     permission_classes = [
#         IsOwnerOrReadOnly
#     ]

#     def get_object(self, pk):
#         """ View to get a Comment"""
#         try:
#             comment = Comment.objects.get(pk=pk)
#             self.check_object_permissions(self.request, comment)
#             return comment
#         except Comment.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         """ get comment """
#         comment = self.get_object(pk)
#         serializer = CommentSerializer(comment, context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, pk):
#         """ edit a comment """
#         comment = self.get_object(pk)
#         serializer = CommentSerializer(
#             comment, data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         """ delete a comment """
#         comment = self.get_object(pk)
#         comment.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )
