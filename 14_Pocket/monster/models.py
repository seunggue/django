from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Monster(models.Model):
    choice = models.CharField(max_length=100)
    content_title = models.CharField(max_length=100) 
    monster_name = models.CharField(max_length=100)
    monster_image = ProcessedImageField(
            processors=[ResizeToFill(300, 300)],
            format='JPEG',
            options = {'quality': 100},
            upload_to = 'monster'
    )
    monster_detail = models.CharField(max_length=100)
    monster_size = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name= 'like_monsters')


class Comment(models.Model):
    content = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
