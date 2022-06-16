from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

@api_view(['GET'])
def getDataAll(resquest):
    if resquest.method == 'GET':
        data = ClientData.objects.all()
        data_serializer = ClientDataSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)

@api_view(['GET'])
def getDataActive(resquest):
    if resquest.method == 'GET':
        data = ClientData.objects.filter(is_active=True)
        data_serializer = ClientDataSerializer(data, many=True)
        if data is True:
            return JsonResponse(data_serializer.data, safe=False)
        else:
            return JsonResponse(data_serializer.data, safe=False)

@api_view(['POST'])
def postData(resquest):
    if resquest.method=='POST':
        data = JSONParser().parse(resquest)
        data_serializer = ClientDataSerializer(data=data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)



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
