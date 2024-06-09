from django.urls import path
from .views import materials_fi,materials_en

urlpatterns = [
    path('en/materials', materials_en, name='materials_en'), 
    path('fi/materials', materials_fi, name='materials_fi'), 
]
