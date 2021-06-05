from django.urls import path     
from . import views

urlpatterns = [
    path('welcome', views.index),
    path('logout', views.logout),
    path('showanime',views.anime_pg),
    path('trending',views.trending_pg),
    path('profile',views.profile_pg),
]