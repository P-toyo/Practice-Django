from django.urls import path

from blog.views import BlogListView, BlogDetailView, CategoryBlogListView, TagBlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='post-list'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("category/<str:slug>/", CategoryBlogListView.as_view(), name="category-post-list"),
    path("tag/<str:slug>/", TagBlogListView.as_view(), name="tag-post-list"),
]