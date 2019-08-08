from django.db import models

# Create your models here.
class Nono(models.Model):
    product = models.CharField(max_length=50)
    replace = models.CharField(max_length=50)
    img_url = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
