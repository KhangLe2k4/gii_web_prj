from django.urls import path
from . import views

urlpatterns = [
    path('en/news/', views.news_en, name='news_en'),
    path('fi/news/', views.news_fi, name='news_fi'),
    path('select-language/<str:language_code>/', views.news_select_language, name='news_select_language'),
]
