from django.shortcuts import render, redirect, get_object_or_404

def materials_en(request):
    return render(request,'materials_en.html')

def materials_fi(request):
    return render(request,'materials_fi.html')

#
