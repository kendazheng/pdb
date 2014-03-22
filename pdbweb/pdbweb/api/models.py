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
    author = models.ForeignKey(User,related_name='article')
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=20,choices=TAG_CHOICE,default='ENTERTAINMENT')
    index = models.URLField(max_length=500)
    summary = models.TextField(max_length=1000)
    publish_date = models.DateTimeField(auto_now=True)
    publish_state = models.BooleanField()

    def __unicode__(self):
        return '%s:%s' %(self.author, self.title)

class Content(models.Model):
    article = models.ForeignKey(Article, related_name='contents')
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    class Meta:
        unique_together = ('article', 'title')

    def __unicode__(self):
        return '%s:%s' %(self.article, self.title)

class Media(models.Model):
    MEDIA_CHOICE = (
        ('IMAGE','image'),
        ('VIDEO','video')
    )
    content = models.ForeignKey(Content, related_name='medias')
    src = models.URLField(max_length=500)
    media_type = models.CharField(max_length=10,choices=MEDIA_CHOICE,default='IMAGE') 
   
    class Meta:
        unique_together = ('content', 'src')
     
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

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    #artist = models.CharField(max_length=100)
    artist = models.ForeignKey(User, related_name='artist')
    

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks')
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)
