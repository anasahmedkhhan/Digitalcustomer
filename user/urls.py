
from django.contrib import admin
from django.urls import path
from user.views import *
app_name = "user"



urlpatterns = [
    path('', userHomepage, name='homepage'),
    path('uploadDoc', uploadDocument, name='uploadDoc'),

]
