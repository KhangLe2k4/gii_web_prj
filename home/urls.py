from django.urls import path
from .views import home_en, home_fi, home, select_language,post_en,post_fi

urlpatterns = [
    path('en/', home_en, name='home_en'), 
    path('fi/', home_fi, name='home_fi'), 
    path('',home,name='home_en'),
    path('fi/post/<int:post_id>/<str:post_title>/',post_fi,name='post_fi'),
    path('en/post/<int:post_id>/<str:post_title>/', post_en, name='post_en'),
    path('<str:language_code>/', select_language, name='select_language'),
]
