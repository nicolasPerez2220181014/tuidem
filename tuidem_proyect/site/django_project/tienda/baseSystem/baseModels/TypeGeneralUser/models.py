from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
import threading
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime
from mongoengine import Document, DateTimeField, BooleanField, StringField, ReferenceField, IntField

class TypeGeneralUser(models.Model):
    name = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.name
