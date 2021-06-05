from django.db import models
# from django.db.models.enums import Choices
from user_app.models import Users
from enum import Enum 




class Animes(models.Model):
    title=models.CharField(max_length=45)
    desc=models.TextField()
    release_date=models.DateField()
    pic_url=models.URLField()
    trailer_url=models.URLField()
    pic_bg=models.URLField()
    user_id_a=models.ForeignKey(Users,related_name="u_anime",on_delete=models.CASCADE)
    fav_list=models.ManyToManyField(Users,related_name="liked_a")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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