from django.db import models
from tienda.models.store.models import Store

class Product(models.Model):
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def get(cls, product_id):
        return cls.objects.get(id=product_id)

    @classmethod
    def update(cls, product_id, **kwargs):
        product = cls.objects.get(id=product_id)
        for field, value in kwargs.items():
            setattr(product, field, value)
        product.save()
        return product

    @classmethod
    def delete(cls, product_id):
        cls.objects.filter(id=product_id).delete()
