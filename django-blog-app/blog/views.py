from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from blog.models import Task

class BlogListView(ListView):
    model = Task
    template_name = "blog/post_list.html"

class BlogDetailView(DetailView):
    model = Task
    template_name = "blog/post_detail.html"

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.is_published or self.request.user.is_authenticated:
            return post
        else:
            raise Http404