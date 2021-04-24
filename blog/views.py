from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, Comments
from .forms import CommentForm
from django.contrib.auth.models import User


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


# class BlogDetailsView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments
    })


class CommentListView(ListView):
    model = Comments
    template_name = 'comments.html'


def comment_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments
    return render(request, 'comments.html', {
        'comments': comments.all()
    })


def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('comments', pk=pk)
    else:
        comment_form = CommentForm()
    return render(request, 'create_comment.html', {
        'user': user.get_username(),
        'comment_form': comment_form
    })


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('home')


class BlogEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'author', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
