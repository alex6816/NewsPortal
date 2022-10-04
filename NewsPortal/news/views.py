from pyexpat.errors import messages

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, ProfilForm
from .models import *
from .filters import PostFilter
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class NewsList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


def subscribe(request, pk):
    context = {
        'user': request.user,
        'cat': Category.objects.get(id=pk),
        'is_subscribed': Category.objects.get(id=pk).subscribers.filter(id=request.user.id).exists()
    }
    return render(request, 'news/subscribe.html', context)


# подписка на группу
@login_required
def add_subscribe(request, pk):
    user = request.user
    cat = Category.objects.get(id=pk)
    is_subscribed = cat.subscribers.filter(id=user.id).exists()

    if not is_subscribed:
        cat.subscribers.add(user)
    return redirect('/news/')


# функция отписки от группы
@login_required
def del_subscribe(request, pk):
    user = request.user
    cat = Category.objects.get(id=pk)
    is_subscribed = cat.subscribers.filter(id=user.id).exists()

    if is_subscribed:
        cat.subscribers.remove(user)
    return redirect('/news/')


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post', 'news.change_post',)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post', 'news.change_post',)


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ProfilUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProfilForm
    model = User
    template_name = 'profil.html'
    success_url = '/'
    success_message = 'User profile updated successfully.'

    def get_object(self, **kwargs):
        return self.request.user
