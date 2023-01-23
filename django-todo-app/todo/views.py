from django.shortcuts import render
from django.views.generic import ListView, DetailView

from todo.models import Task

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"

class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"