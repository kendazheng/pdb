import logging
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

# Create your views here.
def login(request):
    logger = logging.getLogger('pdbweb')
    username = request.POST.get('username', 'no name')
    logger.info(username)
    password = request.POST.get('password', 'no passwd')
    logger.info(password)
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return HttpResponse('OK')
    else:
        return HttpResponse('Error')
