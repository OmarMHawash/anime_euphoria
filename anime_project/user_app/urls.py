from django.urls import path     
from . import views
urlpatterns = [
    path('', views.loginRender),
    path('login', views.login),
    path('register', views.register),

]