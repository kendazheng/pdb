from rest_framework import serializers
from django.contrib.auth.models import User
from pdbweb.api.models import *

class LoginObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.username = attrs.get('username',instance.username)
            instance.password = attrs.get('password',instance.password)
            return instance

        return LoginObject(**attrs)    

class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','email') 

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('src', 'media_type')

class ContentSerializer(serializers.ModelSerializer):
    medias = MediaSerializer(many=True)    
    class Meta:
        model = Content
        fields = ('title', 'desc', 'medias')

class ArticleSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)
    author = serializers.SlugRelatedField(slug_field='username')
    class Meta:
        model = Article
        #fields = ('id', 'title', 'author', 'index', 'summary', 'publish_date', 'publish_state', 'contents','tag')
        read_only_fields = ('id',)

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order', 'title', 'duration')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)
    artist = serializers.SlugRelatedField(slug_field='username')
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')
