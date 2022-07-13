from rest_framework import serializers
from .models import ResponsibleData

class ResponsibleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsibleData
        fields = [
            'id','dni','type_identification_document','fisrt_name', 
            'second_name', 'father_surname', 'mother_surname', 'mobile',
            'procedure'
        ]
    