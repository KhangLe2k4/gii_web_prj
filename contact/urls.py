from django.urls import path
from .views import contact_fi,contact_en

urlpatterns = [
    path('en/contact', contact_en, name='contact_en'), 
    path('fi/contact', contact_fi, name='contact_fi'), 
]
