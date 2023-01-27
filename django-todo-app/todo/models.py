from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField("タイトル", max_length=30)
    discription = models.TextField("説明", blank=True)
    deadline = models.DateField("締切日")

    def __str__(self):
        return self.title