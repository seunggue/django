from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    due_date = models.DateField()
    author = models.CharField(max_length=10)
