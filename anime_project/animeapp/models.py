from django.db import models
# from django.db.models.enums import Choices
from user_app.models import Users
from enum import Enum 

class AnimeManager(models.Manager):
    def basic_anime(self, postData):
        errors = {}
        if len(postData['title']) <3:
            errors["title"] = "Anime name should be at least 3 characters"
        if len(postData['desc']) < 125 :
            errors["desc"] = "password should be at least 125 characters"        
        if postData['rating'] >= 0 and postData['rating'] <= 10 :
            errors["rating"] = "Rating should be between 0 and 10"
        if len(postData['pic_url']) > 5 :
            errors["pic_url"] = "You should enter url "
        if len(postData['trailer_url']) > 5 :
            errors["trailer_url"] = "You should enter trailer url "    
        if len(postData['pic_bg']) > 5 :
            errors["pic_bg"] = "You should enter background url "  
    def basic_comments(self, postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors["email"] = " email should be at least 1 characters"
        return errors
    def basic_category(self, postData):
        errors = {}
        if len(postData['category']) != "":
            errors["category"] = "category not in list"
        return errors

class Animes(models.Model):
    class Rating(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4 
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9 
        TEN = 10 
    title=models.CharField(max_length=45)
    desc=models.TextField()
    release_date=models.DateField()
    pic_url=models.URLField()
    trailer_url=models.URLField()
    pic_bg=models.URLField()
    rating=models.IntegerField(default=Rating.ZERO, null=True,choices=Rating.choices)
    user_id_a=models.ForeignKey(Users,related_name="u_anime",on_delete=models.CASCADE)
    fav_list=models.ManyToManyField(Users,related_name="liked_a")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AnimeManager()

class Comments(models.Model):
    comment=models.TextField()
    user_id= models.ForeignKey(Users, related_name="u_comment",on_delete=models.CASCADE)
    anime_id=models.ForeignKey(Animes, related_name="a_comment",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    Action = 'AC'
    Adventure = 'AV'
    Comedy ='CM'
    Drama = 'DR'
    Horror = 'HO'
    Highschool = 'HS'
    Magic = 'MG'
    Supernatural = 'SN'
    Shounen = 'SH'
    Slice_of_life = 'SL'
    Psycological = 'SY'
    CATEGORY_CHOICES=[
        (Action,'Action'),
        (Adventure,'Adventure'),
        (Comedy,'Comedy'),
        (Drama,'Drama'),
        (Horror,'Horror'),
        (Highschool,'Highschool'),
        (Magic,'Magic'),
        (Shounen,'Shounen'),
        (Slice_of_life,'Slice of Life'),
        (Supernatural,'Supernatural'),
        (Psycological ,'Psychological')
    ]
    category=models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    genre = models.ForeignKey(Animes,related_name="anime_category",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)