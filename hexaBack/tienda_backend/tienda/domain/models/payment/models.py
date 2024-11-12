from django.db import models
from tienda.models.order.models import Order

class Payment(models.Model):
    order = models.ForeignKey(Order, related_name='payments', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f'Payment {self.id} - {self.amount} via {self.payment_method}'

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def get(cls, payment_id):
        return cls.objects.get(id=payment_id)

    @classmethod
    def update(cls, payment_id, **kwargs):
        payment = cls.objects.get(id=payment_id)
        for field, value in kwargs.items():
            setattr(payment, field, value)
        payment.save()
        return payment

    @classmethod
    def delete(cls, payment_id):
        cls.objects.filter(id=payment_id).delete()
