from tienda.views.base import BaseViewSet
from tienda.models.store.models import Store
from tienda.serializers.store import StoreSerializer

class StoreViewSet(BaseViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
