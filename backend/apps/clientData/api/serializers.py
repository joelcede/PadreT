from rest_framework import serializers
from .models import IdentificationDocument, ClientData

class IdentificationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationDocument
        fields = '__all__'