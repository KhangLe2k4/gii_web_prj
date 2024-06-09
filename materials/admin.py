from django.contrib import admin

from .models import EnDocument,FiDocument,EnCategory,FiCategory

admin.site.register(EnCategory)
admin.site.register(FiCategory)
admin.site.register(EnDocument)
admin.site.register(FiDocument)