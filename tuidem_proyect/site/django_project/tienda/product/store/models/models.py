from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
import threading
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime
from mongoengine import Document, DateTimeField, BooleanField, StringField, ReferenceField, IntField
from baseSystem.models.models import *

class Store(Base):  # Hereda de Base
    website_url = models.URLField(null=True, blank=True)
    opening_hours = models.CharField(max_length=255, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    category = models.CharField(max_length=255)
    stock_management = models.BooleanField(default=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    shipping_policy = models.TextField(null=True, blank=True)
    return_policy = models.TextField(null=True, blank=True)
    store_type = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(UserGeneral, on_delete=models.SET_NULL, null=True, related_name='managed_stores')

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(UserGeneral, related_name='orders', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='orders', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='order', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('completed', 'Completed')], default='pending')
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_person = models.ForeignKey(UserGeneral, related_name='assigned_orders', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Order {self.id} - {self.status}'

class Review(models.Model):
    customer = models.ForeignKey(UserGeneral, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    store = models.ForeignKey(Store, related_name='store_reviews', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.customer} - {self.rating}'
