from tienda.views.base import BaseViewSet
from tienda.models.payment.models import Payment
from tienda.serializers.payment import PaymentSerializer

class PaymentViewSet(BaseViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
