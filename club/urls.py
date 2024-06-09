from django.urls import path
from .views import club_en,club_fi

urlpatterns = [
    path('en/club', club_en, name='club_en'), 
    path('fi/club', club_fi, name='club_fi'), 
]
