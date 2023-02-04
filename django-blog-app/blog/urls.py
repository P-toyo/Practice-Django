from django.urls import path

from blog.views import BlogListView, BlogDetailView, CategoryPostListView

urlpatterns = [
    path('', BlogListView.as_view(), name='post-list'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("category/<str:slug>/", CategoryPostListView.as_view(), name="category-post-list"),
]
