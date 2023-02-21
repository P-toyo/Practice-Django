from django.urls import path

from blog.views import (
    BlogListView,
    BlogDetailView,
    CategoryBlogListView,
    TagBlogListView,
    SearchBlogListView,
    CommentCreateView,
    CommentDeleteView,
    ReplyCreateView,
)

urlpatterns = [
    path('', BlogListView.as_view(), name='post-list'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("category/<str:slug>/", CategoryBlogListView.as_view(), name="category-post-list"),
    path("tag/<str:slug>/", TagBlogListView.as_view(), name="tag-post-list"),
    path("search/", SearchBlogListView.as_view(), name="search-post-list"),
    path("comment/<int:post_pk>/", CommentCreateView.as_view(), name="comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
    path("reply/<int:comment_pk>/", ReplyCreateView.as_view(), name="reply"),
]