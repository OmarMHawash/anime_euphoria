from django.shortcuts import render,redirect,HttpResponse

def index(request):
    if 'user' in request.session:
        return render(request,'homepage.html')
def anime_pg(request):
    return render(request,"anime_pg.html")
def trending_pg(request):
    return render(request,"trending.html")  

def profile_pg(request):
    return render(request,"profile.html")  
def logout(request):
    if 'user' in request.session:
        request.session.clear()
    return redirect('/')