from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    TAG_CHOICE = (
        ('ENTERTAINMENT','entertainment'),
        ('SPORT','sport'),
        ('CULTURE','culture'),
        ('TRAVEL','travel'),
        ('TECHNOLOGY','technology'),
        ('FOOD','food'),
        ('FASHION','fashion'),
        ('OTHERS','others')
    )
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=20,choices=TAG_CHOICE,default='ENTERTAINMENT')
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
        ('VIDEO','video')
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
