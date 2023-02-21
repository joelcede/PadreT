from rest_framework import serializers

from .models import GeneralProcedure
from ...clientData.api.serializers import OwnerSerializer

class GeneralProcedureSerializer(serializers.ModelSerializer):
    client_data = OwnerSerializer(many=True, read_only=True)

    class Meta:
        model = GeneralProcedure
        fields = (
            'id','client_data', 'successfull_job',
            'active', 'progress', 'id_house'
        )
    