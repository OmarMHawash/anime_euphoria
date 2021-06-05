from django.db import models
from animeapp.models import *
import re 

class Users(models.Model):
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    p_pic=models.URLField(max_length=255)
    role=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
