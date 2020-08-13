from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from .models import Post
from django.template import RequestContext
# Create your views here.


def homepage(request):

    return render(request, 'instaclone/homepage.html',)


class PostListView(ListView):
    model = Post
    template_name = 'instaclone/homepage.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    template_name = 'instaclone/post_form.html'
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
