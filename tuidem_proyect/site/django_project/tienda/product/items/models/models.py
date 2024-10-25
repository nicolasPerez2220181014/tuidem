from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
import threading
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime
from mongoengine import Document, DateTimeField, BooleanField, StringField, ReferenceField, IntField
from baseSystem.models.models import *

class Product(models.Model):
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    sender = models.ForeignKey(UserGeneral, related_name='sent_packages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(UserGeneral, related_name='received_packages', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dimensions = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending')
    delivery_date = models.DateTimeField(null=True, blank=True)
    tracking_number = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_person = models.ForeignKey(UserGeneral, related_name='deliveries', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Package {self.tracking_number} - {self.status}'
