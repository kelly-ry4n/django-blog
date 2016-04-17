from django.shortcuts import render
from django.views.generic import View
from django.http import Http404

from blog.models import Post, Tag
from blog.utils import get_colors_for_base

class PostView(View):

    def get(self, request, pk, slug, color=None):

        post = Post.objects.get(pk=pk)

        if not post.is_published:
            raise Http404()

        nav_posts = Post.objects.filter(is_published=True)

        ctx = {
            'post':post,
            'nav_posts':nav_posts,
            'color':color,
        }

        return render(request, 'post.html', ctx)


class PostListView(View):

    def get(self, request, color=None):

        posts = Post.objects.filter(is_published=True).order_by('-published')[:3]
        nav_posts = Post.objects.filter(is_published=True).order_by('title')

        ctx = {
            'nav_posts':nav_posts,
            'posts':posts,
            'color':color,
        }

        return render(request, 'post_list.html', ctx)

class CSSView(View):

    def get(self, request, base_color=None):


        if base_color is None:
            colors = {
                'base':'#7F2900',
                'light':'#FF864C',
                'bright':'#FF5200',
                'dark':'#7F4326',
                'saturated':'#CC4200',
            }
        else:
            colors = get_colors_for_base(base_color)

        ctx = {'colors':colors}
        rsp = render(request, 'screen.css', ctx, content_type="text/css")

        return rsp
