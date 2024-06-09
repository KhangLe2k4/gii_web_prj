from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import FileExtensionValidator

class EnHomePost(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField()
    image=models.ImageField(upload_to='media/',  validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif','jfif'])], blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()
    
class FiHomePost(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField()
    image=models.ImageField(upload_to='../static/img/',  validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif','jfif'])], blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    telephone_num=models.CharField(max_length=10,blank=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    company_email=models.CharField(max_length=40,blank=True)
    company_address=models.CharField(max_length=50,blank=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    public=models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name','last_name']

    def __str__(self):
        return self.user_name