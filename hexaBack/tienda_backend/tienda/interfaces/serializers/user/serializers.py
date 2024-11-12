from rest_framework import serializers
from tienda.models.user.models import UserGeneral, Company, TypeGeneralUser

class UserGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGeneral
        fields = ['id', 'username', 'email', 'timezone', 'profile_picture', 'type_user']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'site_url', 'identification', 'business_name', 'email', 'movil', 'alt_phone']

class TypeGeneralUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGeneralUser
        fields = ['id', 'name', 'rol']
