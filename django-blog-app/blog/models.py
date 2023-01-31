from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField("タイトル", max_length = 200)
    content = models.TextField("本文")
    created_at = models.DateTimeField("作成日", auto_now_add = True)
    updated_at = models.DateTimeField("更新日", auto_now = True)
    is_published = models.BooleanField("公開設定", default = False)

    def __str__(self):
        return self.title