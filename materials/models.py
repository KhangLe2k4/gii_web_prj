from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator


class EnCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class FiCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class EnDocument(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    public = models.BooleanField(default=False)
    categories = models.ManyToManyField(EnCategory)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    document=models.FileField(upload_to='pdfs/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])],blank=True,null=True)

    def __str__(self):
        return self.title

class FiDocument(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    public = models.BooleanField(default=False)
    categories = models.ManyToManyField(FiCategory)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title