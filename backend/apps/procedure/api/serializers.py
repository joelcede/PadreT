from rest_framework import serializers

from apps.clientData.api.models import ClientData
from .models import TypeProcedure, GeneralProcedure
from ...clientData.api.serializers import ClientDataSerializer
from ...technicalSupportData.api.serializers import ResponsibleDataSerializer

class TypeProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProcedure
        fields = ('id', 'name')

class GeneralProcedureSerializer(serializers.ModelSerializer):
    type_procedure = TypeProcedureSerializer(many=True, read_only=True)
    client_data = ClientDataSerializer(many=True, read_only=True)
    responsible_technical = ResponsibleDataSerializer(many=True, read_only=True)

    class Meta:
        model = GeneralProcedure
        fields = (
            'id', 'type_procedure' ,'client_data', 'responsible_technical' , 'successfull_job' ,'active'
        )
    