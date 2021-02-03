from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    cnic = models.CharField(max_length=16)
    phoneNo = models.CharField(max_length=30)
    userId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)