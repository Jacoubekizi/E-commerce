from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractUser
from .managers import CustomManagers
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="email address", max_length=150, unique=True)
    username = models.CharField(verbose_name="Username", max_length=200)
    # mobile_phone = models.BigIntegerField(unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomManagers()

    def __str__(self):
        return self.username
    
    @property
    def is_admin(self):
        return self.is_staff