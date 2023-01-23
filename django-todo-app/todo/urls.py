from django.urls import path

from todo.views import TaskListView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail')
]
