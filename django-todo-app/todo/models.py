from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    discription = models.TextField(blank=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title