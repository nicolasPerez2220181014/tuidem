from rest_framework import serializers
from tienda.models.order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'store', 'total_price', 'status', 'order_date']
