from rest_framework import serializers
from django.contrib.auth.models import User

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
        field = ('username', 'password','email') 
