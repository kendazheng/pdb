from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)
    title = models.CharField(max_length=200)
    index = models.URLField(max_length=500)
    publish_date = models.DateTimeField(auto_now=True)
    publish_state = models.BooleanField()

    def __unicode__(self):
        return '%s:%s' %(self.author, self.title)

class Content(models.Model):
    article = models.ForeignKey(Article)
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __unicode__(self):
        return '%s:%s' %(self.article, self.title)

class Media(models.Model):
    MEDIA_CHOICE = (
        ('IMAGE','image'),
        ('VEDIO','vedio')
    )
    content = models.ForeignKey(Content)
    src = models.URLField(max_length=500)
    media_type = models.CharField(max_length=10,choices=MEDIA_CHOICE,default='IMAGE') 
    
    def __unicode__(self):
        return '%s:%s' %(self.content,self.media_type)

class Comment(models.Model):
    article = models.ForeignKey(Article)
    father = models.ForeignKey('self') 
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User)

class Draft(models.Model):
    author = models.ForeignKey(User)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return '%s:%s' %(self.author,self.article)
