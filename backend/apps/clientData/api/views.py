from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from ...clientData.api.models import CadastralData, HouseClientData, MunicipalAccountData, OwnerData, PersonData, ResponsibleData
from ...clientData.api.serializers import CadastralSerializer, HousesClientSerializer, MunicipalAccountSerializer, OwnerSerializer, PersonSerializer

"""PERSONS"""
@api_view(['GET'])
def get_PersonData(resquest):
    if resquest.method == 'GET':
        data = PersonData.objects.all()
        data_serializer = PersonSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def get_OwnerData(resquest):
    if resquest.method == 'GET':
        data = OwnerData.objects.all()
        data_serializer = OwnerSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)


@api_view(['POST'])
def post_PersonData(resquest):
    if resquest.method == 'POST':
        data = PersonSerializer(data=resquest.data)
        if data.is_valid() and data.save():
            return JsonResponse(data.data, status=201)
        return JsonResponse(data.errors, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=405)


@api_view(['POST'])
def create_ownerData(resquest):
    if resquest.method == 'POST':
        dataOwner = OwnerSerializer(data=resquest.data)
        if dataOwner.is_valid() and dataOwner.save():
            return JsonResponse(dataOwner.data, status=status.HTTP_201_CREATE)
        return JsonResponse(dataOwner.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error': 'Metodo no soportado'}, status=status.HTTP_405_METHOD_NOT_ALLOWEDs)

"""OWNERS"""
@api_view(['GET'])
def get_OwnerData(resquest):
    if resquest.method == 'GET':
        data = OwnerData.objects.all()
        data_serializer = OwnerSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def get_OwnerDataIsPrincipal(resquest):
    if resquest.method == 'GET':
        data = OwnerData.objects.filter(is_principal=True)
        data_serializer = OwnerSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def get_HousesData(resquest):
    if resquest.method == 'GET':
        data = HouseClientData.objects.all()
        data_serializer = HousesClientSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def get_CadastralData(resquest):
    if resquest.method == 'GET':
        data = CadastralData.objects.all()
        data_serializer = CadastralSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

def get_MunicipalAccountData(resquest):
    if resquest.method == 'GET':
        data = MunicipalAccountData.objects.all()
        data_serializer = MunicipalAccountSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

def get_ResponsibleData(resquest):
    if resquest.method == 'GET':
        data = ResponsibleData.objects.all()
        data_serializer = MunicipalAccountSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)
