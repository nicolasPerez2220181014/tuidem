from tienda.views.base import BaseViewSet
from tienda.models.order.models import Order
from tienda.serializers.order import OrderSerializer

class OrderViewSet(BaseViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
