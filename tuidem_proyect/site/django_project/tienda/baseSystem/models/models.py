from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
import threading
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime
from mongoengine import Document, DateTimeField, BooleanField, StringField, ReferenceField, IntField

# Base django postgrest

class Base(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    company = models.IntegerField()  # Identificador de compañía
    name = models.CharField(max_length=255)
    alive = models.BooleanField(default=True)
    created_by = models.ForeignKey('UserGeneral', related_name='created_bases', on_delete=models.SET_NULL, null=True)
    last_edit_user = models.ForeignKey('UserGeneral', related_name='edited_bases', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey('UserGeneral', related_name='owned_bases', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

class Person(models.Model):
    name = models.CharField(max_length=255)
    identification = models.CharField(max_length=50, unique=True)
    movl = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Company(models.Model):
    site_url = models.URLField(null=True, blank=True)
    identification = models.CharField(max_length=50, unique=True)
    business_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    movil = models.CharField(max_length=50, null=True, blank=True)
    alt_phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.business_name


#Base mongo