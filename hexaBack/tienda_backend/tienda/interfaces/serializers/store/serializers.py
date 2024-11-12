from rest_framework import serializers
from tienda.models.store.models import Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'description', 'website_url', 'opening_hours', 'rating', 'category', 'stock_management', 'tax', 'shipping_policy', 'return_policy', 'store_type', 'company']
