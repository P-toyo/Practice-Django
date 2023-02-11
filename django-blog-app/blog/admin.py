from django.contrib import admin
from blog.models import Task, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "updated_at", "is_published")
    search_fields = ("title", "content")
    list_filter = ("category",)

admin.site.register(Task, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)