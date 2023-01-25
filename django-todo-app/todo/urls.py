from django.urls import path

from todo.views import TaskListView, TaskDetailView, TaskCreateView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/new/', TaskCreateView.as_view(), name='task-new'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit')
]
