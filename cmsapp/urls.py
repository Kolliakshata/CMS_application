from django.urls import path
from .views import (
    UserCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    LikeCreateView,
    LikeDetailView,
    LikeUpdateView,
    LikeDeleteView,
    PostListView,
)


urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('posts/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('likes/', LikeCreateView.as_view(), name='like-create'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),
    path('likes/<int:pk>/update/', LikeUpdateView.as_view(), name='like-update'),
    path('likes/<int:pk>/delete/', LikeDeleteView.as_view(), name='like-delete'),
    path('posts-with-likes/', PostListView.as_view(), name='post-list'),
]