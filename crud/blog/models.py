from django.db import models
from django.utils import timezone

# Create your models here.
# 모델을 만들 때는 대문자로 해주는 것이 관습
class Post(models.Model):
    title = models.CharField(max_length=200,)
    img = models.FileField(null=True)
    contents = models.TextField()
    price = models.FloatField(default=1,)
    SCORES = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )
    score = models.CharField(max_length=200, choices=SCORES,
        )
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    