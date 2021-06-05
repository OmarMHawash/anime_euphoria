from django.db import models
from animeapp.models import *
import re 
class UserManager(models.Manager):
    def basic_reg(self, postData):
        errors = {}
        if len(postData['username']) <3:
            errors["username"] = "last name should be at least 3 characters"
        if len(postData['password']) < 8 :
            errors["password"] = "password should be at least 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 8:
            errors["email"] = "email should be at least 8 characters"
        return errors
    def basic_log(self, postData):
        errors = {}
        if len(postData['email']) < 8:
            errors["email"] = " email should be at least 8 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "password should be at least 8 characters"
        return errors

class UserManager(models.Manager):
    def basic_reg(self, postData):
        errors = {}
        if len(postData['username']) <3:
            errors["last_name"] = "last name should be at least 3 characters"
        if len(postData['passwd']) < 8 :
            errors["passwd"] = "password should be at least 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 8:
            errors["email"] = "email should be at least 8 characters"
        return errors
    def basic_log(self, postData):
        errors = {}
        if len(postData['email']) < 8:
            errors["email"] = " email should be at least 8 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "password should be at least 8 characters"
        return errors

class Users(models.Model):
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    p_pic=models.URLField()
    role=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
    objects=UserManager()
=======
    objects = UserManager()
>>>>>>> 31f7d412b4e0c9d68bb76cdbce235e18ed1d0a90
