from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import EnPost, FiPost

def news_en(request):
    posts = EnPost.objects.filter(public=1).order_by('-post_date').all()
    page = Paginator(posts, 3)
    page_list=request.GET.get('page')
    page=page.get_page(page_list)
   
    context = {'page': page}
    return render(request, 'news_en.html', context)

def news_fi(request):
    posts = FiPost.objects.filter(public=1).order_by('-post_date')[:6]
    context = {'posts': posts}
    return render(request, 'news_fi.html', context)

def news_select_language(request, language_code):
    if language_code == 'en':
        return redirect('/fi/news')
    else:
        return redirect('/en/news')

