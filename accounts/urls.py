
from django.contrib import admin
from django.urls import path
from accounts.views import *

app_name = "accounts"


urlpatterns = [
    path('', homepage, name='homepage'),
    path('signUp',signUpRedirect , name='signUp'),
    path('signIn',signInRedirect, name='signIn'),
    path('registerUser', registerUser, name='registerUser'),
    path('login', login, name='login'),

]
