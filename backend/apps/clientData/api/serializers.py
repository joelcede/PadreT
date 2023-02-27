from rest_framework import serializers
from .models import (
    CadastralModel, PersonModel, OwnerModel, ResponsibleModel,
    MunicipalAccountModel, HouseClientModel
)

class CadastralSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastralModel
        fields = '__all__'


        
class MunicipalAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipalAccountModel
        fields = ['id', 'user', 'password']

class ResponsibleSerializer(serializers.ModelSerializer):
    #responsible_data = PersonSerializer(many=True, read_only=True)
    #house_x_responsible_data = HousesClientSerializer(many=True, read_only=True)

    class Meta:
        model = ResponsibleModel
        fields = '__all__'

    # def create(self, validated_data):
    #     persona_data = validated_data.pop('responsible_data')
    #     persona = PersonModel.objects.create(**persona_data)
    #     responsible = ResponsibleModel.objects.create(persona=persona, **validated_data)
    #     return responsible



class OwnerSerializer(serializers.ModelSerializer):
    #person_data = PersonSerializer(many=True, read_only=True)
    # house_data = HousesClientSerializer(many=True, read_only=True)

    class Meta:
        model = OwnerModel
        fields = '__all__'

    # def create(self, validated_data):
    #     persona_data = validated_data.pop('person_data')
    #     persona = PersonModel.objects.create(**persona_data)
    #     owner = OwnerModel.objects.create(persona=persona, **validated_data)
    #     return owner

class PersonSerializer(serializers.ModelSerializer):
    #person_data = OwnerSerializer()

    class Meta:
        model = PersonModel
        fields = '__all__'


class HousesClientSerializer(serializers.ModelSerializer):
    house_x_owner_data = OwnerSerializer(many=True, read_only=True)
    person_data = PersonSerializer(many=True, read_only=True)
    responsible_data = ResponsibleSerializer(many=True, read_only=True)
    municipal_account_data = MunicipalAccountSerializer(many=True, read_only=True)
    cadastral_data = CadastralSerializer(many=True, read_only=True)

    class Meta:
        model = HouseClientModel
        fields = '__all__'
