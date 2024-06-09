from django.contrib import admin
from .models import User, EnHomePost, FiHomePost

admin.site.register(EnHomePost)
admin.site.register(FiHomePost)
admin.site.register(User)

# Register your models here.
