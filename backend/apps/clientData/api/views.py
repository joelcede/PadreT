from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes

from .models import IdentificationDocument
from .serializers import IdentificationDocumentSerializer


@csrf_exempt
def identificationApi(resquest):
    if resquest.method=='GET':
        identification = IdentificationDocument.objects.all()
        identification_serializer = IdentificationDocumentSerializer(identification,many=True)
        return JsonResponse(identification_serializer.data, safe=False)
    elif resquest.method=='POST':
        identification_data = JSONParser().parse(resquest)
        identification_serializer = IdentificationDocumentSerializer(data=identification_data)
        if identification_serializer.is_valid():
            identification_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)