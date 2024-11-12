from tienda.views.base import BaseViewSet
from tienda.models.user.models import UserGeneral, Company, TypeGeneralUser
from tienda.serializers.user import UserGeneralSerializer, CompanySerializer, TypeGeneralUserSerializer

class UserGeneralViewSet(BaseViewSet):
    queryset = UserGeneral.objects.all()
    serializer_class = UserGeneralSerializer

class CompanyViewSet(BaseViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class TypeGeneralUserViewSet(BaseViewSet):
    queryset = TypeGeneralUser.objects.all()
    serializer_class = TypeGeneralUserSerializer
