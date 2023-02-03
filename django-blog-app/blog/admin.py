from django.contrib import admin
from blog.models import Task, Category, Tag

# Register your models here.
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Tag)