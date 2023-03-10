from __future__ import annotations

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializer import BlogSerializerDelete
from .serializer import BlogSerializerGet
from .serializer import BlogSerializerPost
from .serializer import BlogSerializerPut
from .serializer import CategorySerializerGet
from .serializer import CategorySerializerPost
from apps.blog.models import Blog
from apps.blog.models import BlogView
from apps.blog.models import Category


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerGet
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset().for_user(self.request.user)
        announcement = get_object_or_404(queryset, id=self.kwargs["id"])
        if self.request.user.is_authenticated:
            BlogView.objects.update_or_create(
                announcement=announcement,
                user=self.request.user,
            )
        elif self.request.headers.get("device-id", None):
            BlogView.objects.update_or_create(
                announcement=announcement,
                device_id=self.request.headers.get("device-id", None),
            )

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerPost
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerGet
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerPut
    permission_classes = (IsAuthenticated, IsAdminUser)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerDelete
    permission_classes = (IsAuthenticated, IsAdminUser)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerGet
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerPost
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
