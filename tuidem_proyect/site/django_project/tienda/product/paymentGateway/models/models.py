from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
import threading
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime
from mongoengine import Document, DateTimeField, BooleanField, StringField, ReferenceField, IntField
from baseSystem.models.models import *

class Payment(models.Model):
    order = models.ForeignKey(Order, related_name='payments', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f'Payment {self.id} - {self.amount} via {self.payment_method}'

class PaymentGateway(models.Model):
    name = models.CharField(max_length=255)
    transaction_fee = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')

    def __str__(self):
        return self.name

class StorePaymentGateway(models.Model):
    store = models.ForeignKey(Store, related_name='payment_gateways', on_delete=models.CASCADE)
    gateway = models.ForeignKey(PaymentGateway, related_name='stores', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('store', 'gateway')

    def __str__(self):
        return f'{self.store.name} - {self.gateway.name}'
