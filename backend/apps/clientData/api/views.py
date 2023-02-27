from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from ...clientData.api.models import (
    CadastralModel, PersonModel, OwnerModel, ResponsibleModel,
    MunicipalAccountModel, HouseClientModel
)
from ...clientData.api.serializers import (
    CadastralSerializer, HousesClientSerializer, ResponsibleSerializer,
    MunicipalAccountSerializer, OwnerSerializer, PersonSerializer
)

"""GETS ALLS"""
@api_view(['GET'])
def getCadastralAll(resquest):
    if resquest.method == 'GET':
        data = CadastralModel.objects.all()
        data_serializer = CadastralSerializer(data, many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def getPersonAll(resquest):
    if resquest.method == 'GET':
        data = PersonModel.objects.all()
        data_serializer = PersonSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def getOwnerAll(resquest):
    if resquest.method == 'GET':
        data = OwnerModel.objects.all()
        data_serializer = OwnerSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def getResponsibleAll(resquest):
    if resquest.method == 'GET':
        data = ResponsibleModel.objects.all()
        data_serializer = ResponsibleSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def getMunicipalAccountAll(resquest):
    if resquest.method == 'GET':
        data = MunicipalAccountModel.objects.all()
        data_serializer = MunicipalAccountSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def getHousesClientsAll(resquest):
    if resquest.method == 'GET':
        data = HouseClientModel.objects.all()
        data_serializer = HousesClientSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def get_person_x_owner(resquest, id):
    if resquest.method == 'GET':
        person = PersonModel.objects.get(id=id)
        person_serealizer = PersonSerializer(person)
        return JsonResponse(person_serealizer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

"""POSTS"""
@api_view(['POST'])
def postCadastral(resquest):
    if resquest.method == 'POST':
        data = CadastralSerializer(data=resquest.data)
        if data.is_valid() and data.save():
            return JsonResponse(data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data.errors, status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error': 'metodo no soportado'}, status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def postPerson(resquest):
    if resquest.method == 'POST':
        data = PersonSerializer(data=resquest.data)
        if data.is_valid() and data.save():
            return JsonResponse(data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data.errors, status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error': 'metodo no soportado'}, status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def postOwner(resquest):
    if resquest.method == 'POST':
        data = OwnerSerializer(data=resquest.data)
        if data.is_valid() and data.save():
            return JsonResponse(data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data.errors, status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error': 'metodo no soportado'}, status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def postResponsible(resquest):
    if resquest.method == 'POST':
        data = ResponsibleSerializer(data=resquest.data)
        if data.is_valid() and data.save():
            return JsonResponse(data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data.errors, status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error': 'metodo no soportado'}, status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def postMunicipalAccount(resquest):
    if resquest.method == 'POST':
        data = MunicipalAccountSerializer(data=resquest.data)
        if data.is_valid() and data.save():
            return JsonResponse(data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data.errors, status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error': 'metodo no soportado'}, status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def postHouseClient(resquest):
    if resquest.method == 'POST':
        data = HousesClientSerializer(data=resquest.data)
        if data.is_valid() and data.save():
            return JsonResponse(data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data.errors, status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'error': 'metodo no soportado'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
