from django.shortcuts import render

# Create your views here.
def club_en(request):
    return render(request,'club_en.html')

def club_fi(request):
    return render(request,'club_fi.html')