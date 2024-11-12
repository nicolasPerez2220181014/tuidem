from rest_framework import status, viewsets
from rest_framework.response import Response
from tienda.domain.services import ProductService
from tienda.interfaces.serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = ProductService.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            ProductService.create_product(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = ProductService.get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = ProductService.update_product(pk, request.data)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        ProductService.delete_product(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
