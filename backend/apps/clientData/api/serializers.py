from rest_framework import serializers
from .models import (
    PersonData, MunicipalAccountData, CadastralData,
    HouseClientData, OwnerData, ResponsibleData
)

class CadastralSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastralData
        fields = [
            'id', 'sector', 'apple', 'lot', 'div1', 'div2', 'div3', 'div4', 'cadastral'
        ]

class MunicipalAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipalAccountData
        fields = ['id', 'user', 'password', 'owner_data']


class PersonSerializer(serializers.ModelSerializer):
    #id_person_data = OwnerSerializer(many=True, read_only=True)
    #houses_owner = HousesClientSerializer(many=True, read_only=True)
    class Meta:
        model = PersonData
        fields = [
            'id','dni','type_identification_document','fisrt_name', 'second_name',
            'father_surname', 'mother_surname', 'mobile'#, 'id_person_data'
        ]

class OwnerSerializer(serializers.ModelSerializer):
    person_data = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = OwnerData
        fields = [
            'id', 'id_person_data', 'is_principal',
        ]



class HousesClientSerializer(serializers.ModelSerializer):
    house_cadastral = CadastralSerializer(many=True, read_only=True)
    id_person_x_house_data = PersonSerializer(many=True, read_only=True)
    #ids = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = HouseClientData
        fields = [
            'id', 'image' , 'country','province','town','parish','district',
            'main_road_name', 'cross_road_name', 'coordinates', 'house_cadastral', 'id_person_x_house_data'
        ]



class ResponsibleSerializer(serializers.ModelSerializer):
    house_cadastral = CadastralSerializer(many=True, read_only=True)
    #owner = OwnerDataSerializer(many=True, read_only=True)

    class Meta:
        model = HouseClientData
        fields = [
            'id', 'image' , 'country','province','town','parish','district',
            'main_road_name', 'cross_road_name', 'coordinates','owner', 'house_cadastral'
        ]

