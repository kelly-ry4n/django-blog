from django.shortcuts import render
from django.views.generic import View
from django.http import Http404

from blog.models import Post, Tag

class PostView(View):

    def get(self, request, pk, slug):

        post = Post.objects.get(pk=pk)

        if not post.is_published:
            raise Http404()

        nav_posts = Post.objects.filter(is_published=True)

        ctx = {
            'post':post,
            'nav_posts':nav_posts,
        }

        return render(request, 'post.html', ctx)


class PostListView(View):

    def get(self, request):

        posts = Post.objects.filter(is_published=True).order_by('-published')[:3]
        nav_posts = Post.objects.filter(is_published=True).order_by('title')

        ctx = {
            'nav_posts':nav_posts,
            'posts':posts,
        }

        return render(request, 'post_list.html', ctx)
