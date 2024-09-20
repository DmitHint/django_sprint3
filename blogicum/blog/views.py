from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post, Category
from django.conf import settings


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:settings.POSTS_PER_PAGE]

    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(Post,
                             pub_date__lte=timezone.now(),
                             is_published=True,
                             category__is_published=True,
                             id=pk)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, is_published=True,
                                 slug=category_slug)
    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
