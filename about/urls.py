from django.urls import path
from .views import about_en, about_fi, about_select_language

urlpatterns = [
    path('en/about', about_en, name='about_en'), 
    path('fi/about',about_fi,name='about_fi'),
    path('<str:language_code>/about',about_select_language,name='about_select_language')
    
]
