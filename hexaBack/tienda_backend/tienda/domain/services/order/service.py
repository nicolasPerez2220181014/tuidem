from tienda.models.order.models import Order

class OrderService:
    @staticmethod
    def create(data):
        return Order.objects.create(**data)

    @staticmethod
    def get(order_id):
        return Order.objects.get(id=order_id)

    @staticmethod
    def update(order_id, data):
        order = Order.objects.get(id=order_id)
        for key, value in data.items():
            setattr(order, key, value)
        order.save()
        return order

    @staticmethod
    def delete(order_id):
        order = Order.objects.get(id=order_id)
        order.delete()
