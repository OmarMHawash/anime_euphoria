from django.http.response import JsonResponse
from animeapp.models import Animes
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from user_app.models import *
from django.contrib import messages
from django.db.models import Count
import bcrypt

def index(request):
    # if 'user' in request.session:
        context={
            "background1":Animes.objects.order_by("updated_at")[0:1].get(),
            "background2":Animes.objects.order_by("updated_at")[1:2].get(),
            "background3":Animes.objects.order_by("updated_at")[2:3].get(),
            "background4":Animes.objects.order_by("updated_at")[3:4].get(),
            "animenames":Animes.objects.order_by("updated_at")[0:4],
            "animenames1":Animes.objects.order_by("updated_at")[4:8],
            "animenames2":Animes.objects.order_by("updated_at")[8:12],

            }
        return render(request,'homepage.html',context)
def anime_pg(request,id):
    anime = Animes.objects.get(id=id)
    context = {
        'anime_id':id,
        'this_anime':anime,
        'all_comments':Comments.objects.filter(anime_id=id)
    }
    request.session['anime_id']=id

    return render(request,"anime_pg.html",context)

def addComment(request):
    id = request.session['anime_id']
    if 'user' in request.session:
        Comments.objects.create(comment=request.POST['comment'],user_id=Users.objects.get(id=request.session['user_id']),anime_id=Animes.objects.get(id=id))
        return redirect('/main/anime/'+str(id))
    errors = Users.objects.commentInCheck(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    return redirect('/')

def addLike(request):
    id=request.session['anime_id']
    anime=Animes.objects.get(id=request.session['anime_id'])
    user=Users.objects.get(id=request.session['user_id'])
    if 'user' in request.session:
        anime.fav_list.add(user)
        return redirect('/main/anime/'+str(id))
    errors = Users.objects.likeInCheck(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    return redirect('/')

def deleteLike(request):
    id=request.session['anime_id']
    anime=Animes.objects.get(id=request.session['anime_id'])
    user=Users.objects.get(id=request.session['user_id'])
    if 'user' in request.session:
        anime.fav_list.remove(user)
        return redirect('/main/anime/'+str(id))
    errors = Users.objects.likeInCheck(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    return redirect('/')

def profile_pg_main(request):
    if 'user' in request.session:
        id = request.session['user_id']
        user=Users.objects.get(id=id)
        context ={
            'user':user,
            'user_comments':Comments.objects.filter(user_id=id),
        }
        return render(request,"profile.html",context)
    errors = Users.objects.loggedInCheck(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    return redirect('/')
def trending_pg(request):
    top_liked = Animes.objects.all() \
                .annotate(num_likes=Count('fav_list')) \
                .order_by('-num_likes')
    context={
        'latest_animes': Animes.objects.all().order_by('-id')[:5],
        'hottest_animes': Animes.objects.all().order_by('id')[:5],
        'most_liked':top_liked,
        'last_commented': Comments.objects.all().order_by('-id')[:5],
    }
    return render(request,"trending.html",context)

def update(request,id):
    errors = Animes.objects.basic_update(request.POST)
    user=Users.objects.get(id=id)
    if request.POST["usernameu"]:
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        if len(request.POST["usernameu"]) > 2 :
            user.username=request.POST["usernameu"]
    if request.POST["passwordu"]:
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        if len(request.POST["passwordu"]) > 7 :
            user.password=bcrypt.hashpw(request.POST["passwordu"].encode(), bcrypt.gensalt()).decode()
    if request.POST["url"]:
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        if len(request.POST["url"]) > 5 :
            user.username=request.POST["url"]
    user.save()
    return redirect('/main/profile')

def profile_pg(request,id):
        user=Users.objects.get(id=id)
        context ={
            'user':user,
            'user_comments':Comments.objects.filter(user_id=id),
            'liked':user.liked_a.all()
        }
        return render(request,"profile.html",context)
def logout(request):
    errors = Animes.objects.basic_delete(request.POST)
    if 'user' in request.session:
        request.session.clear()
    if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
    return redirect('/')

def autocomplete(request):
    if 'term' in request.GET:
        qs = Animes.objects.filter(title__istartswith=request.GET.get('term'))
        titles=list()
        for anime in qs:
            titles.append(anime.title)
        return JsonResponse(titles,safe=False)
    return redirect('/main/welcome')

def search(request):
    if request.POST["search"]:
        anime=Animes.objects.filter(title=request.POST["search"])
        animeid=anime[0].id
        print(request.POST["search"])
        return redirect(f"/main/anime/{animeid}")