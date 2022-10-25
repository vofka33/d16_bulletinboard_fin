from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class PostsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    ordering = '-dateCreation'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    queryset = Post.objects.all()