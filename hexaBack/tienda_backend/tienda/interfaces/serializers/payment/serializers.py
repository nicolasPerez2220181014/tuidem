from rest_framework import serializers
from tienda.models.payment.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'payment_date', 'amount', 'payment_method']
