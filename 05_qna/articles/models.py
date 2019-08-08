from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    user = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now_add=True: 작성일자 표시 안해도 자동으로 서버시간(현재시간)을 입력해줌

class Answer(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #CASCADE
