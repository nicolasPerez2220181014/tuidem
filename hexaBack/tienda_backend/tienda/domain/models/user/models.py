from django.db import models
from django.contrib.auth.models import AbstractUser

class TypeGeneralUser(models.Model):
    name = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserGeneral(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    timezone = models.CharField(max_length=255, null=True, blank=True)
    type_user = models.ForeignKey(TypeGeneralUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

class Company(models.Model):
    site_url = models.URLField(null=True, blank=True)
    identification = models.CharField(max_length=50, unique=True)
    business_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    movil = models.CharField(max_length=50, null=True, blank=True)
    alt_phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.business_name
