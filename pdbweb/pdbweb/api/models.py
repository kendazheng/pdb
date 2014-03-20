from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)


class Article(models.Model):
    author = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)
    title = models.CharField(max_length=200) 
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)
    publish_state = models.BooleanField()


class Comment(models.Model):
    article = models.ForeignKey(Article)
    father = models.ForeignKey('self') 
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User)
