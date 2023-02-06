from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.
from blog.models import Task, Category

class BlogListView(ListView):
    model = Task
    template_name = "blog/post_list.html"

    def get_queryset(self):
        posts = super().get_queryset()
        return posts.order_by("-updated_at")

class BlogDetailView(DetailView):
    model = Task
    template_name = "blog/post_detail.html"

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.is_published or self.request.user.is_authenticated:
            return post
        else:
            raise Http404

class CategoryBlogListView(ListView):
    model = Task
    tamplate_name = "blog/post_list.html"

    def get_queryset(self):
        slug = self.kwargs["slug"]
        self.category = get_object_or_404(Category, slug=slug)
        return super().get_queryset().filter(category=self.category)