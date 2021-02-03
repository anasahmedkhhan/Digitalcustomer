from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import *
from django.http import HttpResponse, JsonResponse
# Create your views here.


def userHomepage(request):
    return render(request,'Home\menu.html')


def uploadDocument(request):
    if request.user.is_authenticated:
        return render(request,'Home\\uplodeDocument.html')
