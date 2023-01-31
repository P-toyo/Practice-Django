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