from django.db.models import Count, Q
from blog.models import Category, Tag

def common(request):
    context = {
        "categories": Category.objects.annotate(
            count = Count("task", Q(task__is_published=True))
        ),
        "tags": Tag.objects.all()
    }
    return context
    