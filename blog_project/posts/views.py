from django.shortcuts import render
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



















# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class UserList(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

