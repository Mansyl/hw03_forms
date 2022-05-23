from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView
from .forms import PostForm
from .models import Group, Post


User = get_user_model()


class Posts(models.Model):
    number_of_posts = 10

    class Meta:
        abstract = True


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    number_of_posts = Posts.number_of_posts
    paginator = Paginator(post_list, number_of_posts)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'Последние посты'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    number_of_posts = Posts.number_of_posts
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(post_list, number_of_posts)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': f'Записи сообщества "{group.title}"',
        'page_obj': page_obj,
        'group': group,
    }
    return render(request, 'posts/group_list.html', context)


class AboutTechView(TemplateView):

    template_name = 'app_name/tech.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['just_title'] = 'Очень простая страница'
        context['text_1'] = ('Страница «Технологии»')
        context['just_text'] = ('На создание этой страницы '
                                'у меня ушло пять минут! Ай да я.')
        return context


class AboutAuthorView(TemplateView):

    template_name = 'app_name/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['just_title'] = 'Очень простая страница'
        context['text_1'] = ('Страница «Об авторе»')
        context['just_text'] = ('На создание этой страницы '
                                'у меня ушло пять минут! Ай да я.')
        return context


def profile(request, username):
    number_of_posts = Posts.number_of_posts
    author = get_object_or_404(User, username=username)
    posts = author.posts.all().order_by('-pub_date')
    paginator = Paginator(posts, number_of_posts)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj,
               'posts': posts,
               'author': author, }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    count_posts = Post.objects.select_related('author').filter().count()
    context = {'post': post,
               'count_posts': count_posts,
               }
    return render(request, 'posts/post.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', request.user.username)
    return render(request, 'new.html', {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST, instance=post)
    edit = True
    if form.is_valid():
        post = form.save()
        post.author = request.user
        post.save()
        return redirect('posts:post_detail', post_id)
    else:
        form = PostForm(instance=post)
        context = {'edit': edit,
                   'form': form,
                   'post_id': post_id, }
    return render(request, 'new.html', context)
