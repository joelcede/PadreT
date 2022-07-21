import profile
from rest_framework import serializers
from .models import (
    Person, MunicipalAccount, Cadastral,
    HousesClient, ClientData
)

class CadastralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastral
        fields = [
            'id', 'sector', 'apple', 'lot', 'div1', 'div2', 'div3', 'div4', 'home_client'
        ]

class HousesClientSerializer(serializers.ModelSerializer):
    house_cadastral = CadastralSerializer(many=True, read_only=True)

    class Meta:
        model = HousesClient
        fields = [
            'id', 'image' , 'country','province','town','parish','district',
            'main_road_name', 'cross_road_name', 'coordinates', 'house_cadastral'
        ]

class MunicipalAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipalAccount
        fields = ['id', 'user', 'password', 'client_data']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id','dni','type_identification_document','fisrt_name', 'second_name',
            'father_surname', 'mother_surname', 'mobile', 'is_principal', 'client_data'
        ]

class ClientDataSerializer(serializers.ModelSerializer):
    person_identification = PersonSerializer(many=True, read_only=True)
    municipal_account = MunicipalAccountSerializer(many=True, read_only=True)
    houses_customer = HousesClientSerializer(many=True, read_only=True)

    class Meta:
        model = ClientData
        fields = [
            'id','mail', 'password', 'telephone', 'person_identification', 
            'municipal_account', 'houses_customer', 'procedure'
        ]
