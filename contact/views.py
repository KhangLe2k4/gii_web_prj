from django.shortcuts import render
from home.models import User


def contact_en(request):
    users=User.objects.all()
    context={'users':users}
    return render(request,'contact_en.html',context)

def contact_fi(request):
    return render(request,'contact_fi.html')

