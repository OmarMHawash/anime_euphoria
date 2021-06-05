from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages

<<<<<<< HEAD
def loginRender(request):
    if 'user' in request.session:
        return redirect('/')
    return render(request,'login.html')

def login(request):

    return redirect('/')

def register(request):
    errors = Users.objects.basic_reg(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/profile')
    else:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user_data= {
            'email': email,
            'username': username,
            'password': password,
        }
        request.session['user'] = user_data
        logged_user = Users.objects.create(username=username,password=password,email=email)
        request.session['user_id']=logged_user.id
    return redirect('/')
    
    
=======
def index(request):
    return HttpResponse("this is users page")
>>>>>>> 180869607eb0ff99c76da7715aa65a9c3c8e8ac8
