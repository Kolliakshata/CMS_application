from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import User, Post, Like
from django.db.models import Count


class UserCreateView(CreateView):
    model = User
    fields = ['name', 'email', 'password', ...]  # Add other relevant fields

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['name', 'email', 'password', ...]  # Add other relevant fields

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = '/users/'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'content', 'is_public', ...]  # Add other relevant fields

class PostDetailView(DetailView):
    model = Post
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('author')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'content', 'is_public', ...]  # Add other relevant fields

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

class LikeCreateView(CreateView):
    model = Like
    fields = ['post', 'user']

class LikeDetailView(DetailView):
    model = Like

class LikeUpdateView(LoginRequiredMixin, UpdateView):
    model = Like
    fields = ['post', 'user']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class LikeDeleteView(LoginRequiredMixin, DeleteView):
    model = Like
    success_url = '/likes/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(num_likes=Count('like'))
