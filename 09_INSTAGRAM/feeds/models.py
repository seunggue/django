from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# imagekit: index상에 보이는 image크기 조절할때 사용
# Create your models here.
class Feed(models.Model):
    content = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField()
    image = ProcessedImageField(
        processors= [ResizeToFill(300,300)],
        format= 'PNG',
        options= {'quality':90},
        upload_to= 'feeds'
    )
