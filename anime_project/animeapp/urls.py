from django.urls import path     
from . import views

urlpatterns = [
    path('welcome', views.index),
    path('logout', views.logout),
    path('trending',views.trending_pg),
    path('profile/<int:id>',views.profile_pg),
    path('anime/<int:id>',views.anime_pg),
    path('add_comment',views.addComment),
    path('add_like',views.addLike),
    path('delete_like',views.deleteLike),
    path('update/<int:id>',views.update),
    path('search',views.autocomplete, name='autocomplete'),
    path('searchh',views.search),


]