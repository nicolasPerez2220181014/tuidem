from tienda.models.store.models import Store

class StoreService:
    @staticmethod
    def create(data):
        return Store.objects.create(**data)

    @staticmethod
    def get(store_id):
        return Store.objects.get(id=store_id)

    @staticmethod
    def update(store_id, data):
        store = Store.objects.get(id=store_id)
        for key, value in data.items():
            setattr(store, key, value)
        store.save()
        return store

    @staticmethod
    def delete(store_id):
        store = Store.objects.get(id=store_id)
        store.delete()
