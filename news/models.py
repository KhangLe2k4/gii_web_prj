from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
import os

class EnPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image=models.ImageField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif','jfif'])], blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    id=models.AutoField(primary_key=True)
    public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def delete(self, *args, **kwargs):
        # Delete the associated image file from the media directory
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super(EnPost, self).delete(*args, **kwargs)

class FiPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image=models.ImageField(upload_to='media/',  validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif','jfif'])], blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    id=models.AutoField(primary_key=True)
    public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    