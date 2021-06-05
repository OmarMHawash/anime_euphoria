from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def loginRender(request):
    print("1")
    if 'user' in request.session:
        return redirect('/main/welcome')
    return render(request,'login.html')

def login(request):
    errors = Users.objects.basic_log(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        email=request.POST['email']
        password=request.POST['password']
        users = Users.objects.filter(email=email)
        if len(users) == 0:
            return redirect('/')
        user = users.first()
        if bcrypt.checkpw(password.encode(), user.password.encode()):

            user_data = {
                'username': user.username,
                'password': user.password,
                'email': user.email,
            }
            request.session['user_id']=users[0].id
            request.session['user'] = user_data
            return redirect('/main/welcome')
        else : 
            errors = Users.objects.basic_pass(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            return redirect('/')


def register(request):
    print("3")
    errors = Users.objects.basic_reg(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            
        return redirect('/')
    else:
        username=request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        user_data= {
            'email': email,
            'username': username,
            'password': password,
        }
        request.session['user'] = user_data
        logged_user = Users.objects.create(username=username,password=pw_hash,email=email)
        request.session['user_id']=logged_user.id
    return redirect('/main/welcome')
    
