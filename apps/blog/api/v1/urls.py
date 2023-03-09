from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogGetSerializer, BlogDeleteView, CategoryListView

urlpatterns = [
    path('blog/', BlogListView.as_view()),
    path('blog/<int:pk>/', BlogDetailView.as_view()),
    path('blog/create/', BlogCreateView.as_view()),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view()),
    path('category/', CategoryListView.as_view()),
]