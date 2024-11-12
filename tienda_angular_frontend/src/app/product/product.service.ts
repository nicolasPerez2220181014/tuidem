from tienda.models.product.models import Product

class ProductService:
    @staticmethod
    def create(data):
        return Product.objects.create(**data)

    @staticmethod
    def get(product_id):
        return Product.objects.get(id=product_id)

    @staticmethod
    def update(product_id, data):
        product = Product.objects.get(id=product_id)
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return product

    @staticmethod
    def delete(product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
