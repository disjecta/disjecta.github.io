from django_distill import distill_path

from .views import IndexView, PostView, TagView, StatusView
from .models import Post, Tag

from django.views.generic import TemplateView


def get_index():
    return None


def get_posts():
    for post in Post.objects.published():
        yield {'slug': post.slug}


def get_tags():
    for tag in Tag.objects.all():
        yield {'tag': tag.name}


def get_status():
    return None


urlpatterns = [

    distill_path('',
                 IndexView.as_view(),
                 name='blog-index',
                 distill_func=get_index,
                 distill_file='index.html'),

    distill_path('post/<slug:slug>.html',
                 PostView.as_view(),
                 name='blog-post',
                 distill_func=get_posts),

    distill_path('tag/<slug:tag>.html',
                 TagView.as_view(),
                 name='blog-tag',
                 distill_func=get_tags),

    distill_path('status',
                 TemplateView.as_view(
                    template_name='status.html'
                 ),
                 name='status',
                 distill_func=get_status),

]
