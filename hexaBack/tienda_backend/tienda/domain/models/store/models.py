from django.db import models
from tienda.models.user.models import Company

class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
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

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def get(cls, store_id):
        return cls.objects.get(id=store_id)

    @classmethod
    def update(cls, store_id, **kwargs):
        store = cls.objects.get(id=store_id)
        for field, value in kwargs.items():
            setattr(store, field, value)
        store.save()
        return store

    @classmethod
    def delete(cls, store_id):
        cls.objects.filter(id=store_id).delete()
