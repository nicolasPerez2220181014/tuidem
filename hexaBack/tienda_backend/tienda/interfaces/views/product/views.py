from tienda.views.base import BaseViewSet
from tienda.models.product.models import Product
from tienda.serializers.product import ProductSerializer

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
