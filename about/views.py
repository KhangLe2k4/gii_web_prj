from django.shortcuts import render, redirect

def about_en(request):
    return render(request,"about_en.html")

def about_fi(request):
    return render(request,'about_fi.html')

def about_select_language(request,language_code):
    if language_code=='en':
        return redirect('/en/about')
    else:
        return redirect('/fi/about')
