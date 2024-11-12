from tienda.models.user.models import UserGeneral, Company, TypeGeneralUser

class UserGeneralService:
    @staticmethod
    def create(data):
        return UserGeneral.objects.create(**data)

    @staticmethod
    def get(user_id):
        return UserGeneral.objects.get(id=user_id)

    @staticmethod
    def update(user_id, data):
        user = UserGeneral.objects.get(id=user_id)
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def delete(user_id):
        user = UserGeneral.objects.get(id=user_id)
        user.delete()

class CompanyService:
    @staticmethod
    def create(data):
        return Company.objects.create(**data)

    @staticmethod
    def get(company_id):
        return Company.objects.get(id=company_id)

    @staticmethod
    def update(company_id, data):
        company = Company.objects.get(id=company_id)
        for key, value in data.items():
            setattr(company, key, value)
        company.save()
        return company

    @staticmethod
    def delete(company_id):
        company = Company.objects.get(id=company_id)
        company.delete()

class TypeGeneralUserService:
    @staticmethod
    def create(data):
        return TypeGeneralUser.objects.create(**data)

    @staticmethod
    def get(type_user_id):
        return TypeGeneralUser.objects.get(id=type_user_id)

    @staticmethod
    def update(type_user_id, data):
        type_user = TypeGeneralUser.objects.get(id=type_user_id)
        for key, value in data.items():
            setattr(type_user, key, value)
        type_user.save()
        return type_user

    @staticmethod
    def delete(type_user_id):
        type_user = TypeGeneralUser.objects.get(id=type_user_id)
        type_user.delete()
