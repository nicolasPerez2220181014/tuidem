from tienda.models.payment.models import Payment

class PaymentService:
    @staticmethod
    def create(data):
        return Payment.objects.create(**data)

    @staticmethod
    def get(payment_id):
        return Payment.objects.get(id=payment_id)

    @staticmethod
    def update(payment_id, data):
        payment = Payment.objects.get(id=payment_id)
        for key, value in data.items():
            setattr(payment, key, value)
        payment.save()
        return payment

    @staticmethod
    def delete(payment_id):
        payment = Payment.objects.get(id=payment_id)
        payment.delete()
