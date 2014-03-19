from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from pdbweb.api.serializers import LoginObject, LoginSerializer,\
  RegistrySerializer


# Create your views here.
class AccountView(APIView):
    #resource = AccountResource

    def get(self, request):
        """
        Login an account
        """
        username = request.GET.get('username')
        password = request.GET.get('password')
        data = {
            'username':username,
            'password':password
        }
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return Response({'status':0,'msg':'OK'})
            else:
                return Response({'status':1,'msg':'Username or Password were Incorrect!'})
        else:
            return Response(serializer.errors)

    def post(self, request):
        """
        Create a new account
        """
        username = request.DATA['username']
        password = request.DATA['password']
        email= request.DATA['email']
        data = {
            'username':username,
            'password':make_password(password),
            'email':email
        }
        serializer = RegistrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            login(request, authenticate(username=username,password=password))
            return Response({'status':0,'msg':'OK'}) 
        else:
            #return Response({'status':1,'msg':'Input Format were Incorrect!'})  
            return Response(serializer.errors)
