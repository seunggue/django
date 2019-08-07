from django.db import models

# Create your models here.
#models의 Model을 상속해서 Post에 적용
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)


