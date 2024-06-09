# home/views.py
from django.shortcuts import render, redirect, get_object_or_404
from news.models import EnPost, FiPost
from materials.models import EnCategory, FiCategory
from .models import EnHomePost, FiHomePost

def home(request):
    return redirect('/en')

def home_en(request):
    posts = EnPost.objects.filter(public=True).order_by('-post_date')[:6]
    categories=EnCategory.objects.all()
    homePosts=EnHomePost.objects.all()
    context={'posts':posts,'categories':categories,'homePosts':homePosts}
    return render(request, 'home_en.html',context)

def home_fi(request):
    posts=FiPost.objects.filter(public=True).order_by('-post_date')[:6]
    categories=FiCategory.objects.all()
    homePosts=FiHomePost.objects.all()
    context={'posts':posts,'categories':categories,'homePosts':homePosts}
    return render(request, 'home_fi.html',context)


def post_en(request, post_id, post_title):
    # Retrieve the post using both post_id and post_title
    post = get_object_or_404(EnPost, id=post_id, title=post_title)
    # Render the post detail page
    
    return render(request, 'post_en.html', {'post': post})

def post_fi(request,post_id,post_title):
    post=get_object_or_404(FiPost,id=post_id,title=post_title)
    return render(request, 'post_fi.html', {'post': post})

def select_language(request, language_code):
   
    request.session['language'] = language_code
   
    return redirect(request.META.get('HTTP_REFERER', 'home'))

