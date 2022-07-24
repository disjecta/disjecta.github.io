from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Tag


class IndexView(ListView):

    template_name = 'blog/index.html'
    model = Post
    allow_empty = False
    queryset = Post.objects.published()
    ordering = '-created'
    context_object_name = 'posts'


class PostView(DetailView):

    template_name = 'blog/post.html'
    model = Post


class TagView(DetailView):

    template_name = 'blog/tag.html'
    model = Tag
    slug_url_kwarg = 'tag'
    slug_field = 'name'
