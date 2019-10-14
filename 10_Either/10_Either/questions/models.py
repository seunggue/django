from django.db import models

# Create your models here.
class Question(models.Model):
    pick_1 = models.TextField()
    pick_2 = models.TextField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick_1_count = models.IntegerField()
    pick_2_count = models.IntegerField()
