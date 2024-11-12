from django.db import models
from tienda.models.user.models import UserGeneral
from tienda.models.store.models import Store

class Order(models.Model):
    customer = models.ForeignKey(UserGeneral, related_name='orders', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='orders', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('completed', 'Completed')], default='pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} - {self.status}'

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def get(cls, order_id):
        return cls.objects.get(id=order_id)

    @classmethod
    def update(cls, order_id, **kwargs):
        order = cls.objects.get(id=order_id)
        for field, value in kwargs.items():
            setattr(order, field, value)
        order.save()
        return order

    @classmethod
    def delete(cls, order_id):
        cls.objects.filter(id=order_id).delete()
