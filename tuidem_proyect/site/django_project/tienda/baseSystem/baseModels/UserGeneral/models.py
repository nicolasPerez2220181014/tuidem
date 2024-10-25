from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
import threading
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime
from mongoengine import Document, DateTimeField, BooleanField, StringField, ReferenceField, IntField

from django.contrib.auth.models import AbstractUser

class UserGeneral(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    timezone = models.CharField(max_length=255, null=True, blank=True)
    type_user = models.ForeignKey('TypeGeneralUser', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username
