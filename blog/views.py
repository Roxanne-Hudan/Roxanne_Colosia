from django.shortcuts import render
#create
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# views
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView
from .models import Post, Comentario, Like

# Delete
from django.views.generic.edit import DeleteView


class PostListView(ListView):
    model = Post
    template_name = 'AppCoder/Blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'AppCoder/Blog/post_list.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comentarios'] = post.comentarios.all().order_by('-fecha')
        context['likes_count'] = post.likes.count()

        user = self.request.user
        if user.is_authenticated:
            context['user_liked'] = post.likes.filter(usuario=user).exists()
        else:
            context['user_liked'] = False

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'AppCoder/Blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'AppCoder/Blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('post-list')

    def test_func(self):
        return self.request.user.is_staff
    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'AppCoder/Blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        return self.request.user.is_staff

# Create your views here.
