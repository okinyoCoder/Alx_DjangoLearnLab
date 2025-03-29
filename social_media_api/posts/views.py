from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import generics
from django.core.exceptions import PermissionDenied
from django.contrib.auth import mixins
from rest_framework import filters

#Pagination
class StandardResults(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# CRUD Operations for post
@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_post(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def view_post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['POST'])
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#CRUD operation for Comments 

class CommentListView(generics.ListAPIView):
    pagination_class = StandardResults
    filter_backends = [filters.SearchFilter]

    def get(self, request, **kwargs):
        pk = self.kwargs['pk']
        post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=post)
        paginated_comments = StandardResults().paginate_queryset(
            queryset=comments, request=request)
        serializer = CommentSerializer(paginated_comments, many=True)
        return Response(serializer.data)


class CommentCreateView(APIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    serializer_class = CommentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUpdateView(APIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    def post(self, request):
        serializer = CommentSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            comment = Comment.objects.get(id=request.data['pk'])
            if self.user != request.user:
                raise PermissionDenied(
                    'Only the author can edit or delete this post')
            if comment.author == request.user:
                serializer.update(Comment, serializer.validated_data)
                return Response(serializer.data)
        return Response(serializer.errors, status=400)


class CommentDetailView(APIView):
    def get(self, request):
        comment = Comment.objects.get(id=request.data['id'])
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


class CommentDeleteView(generics.DestroyAPIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)