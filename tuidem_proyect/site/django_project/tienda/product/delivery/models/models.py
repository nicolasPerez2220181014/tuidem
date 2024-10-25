from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
import threading
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime
from mongoengine import Document, DateTimeField, BooleanField, StringField, ReferenceField, IntField
from baseSystem.models.models import *

class UserDeveloper(models.Model):
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    timezone = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    road = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, related_name='developers')

    def __str__(self):
        return self.username
