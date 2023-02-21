from django.http.response import JsonResponse
from apps.clientData.api.models import CadastralData, OwnerData, MunicipalAccountData, PersonData, HouseClientData
from apps.clientData.api.serializers import (
    CadastralSerializer, OwnerSerializer, HousesClientSerializer, 
    MunicipalAccountSerializer, PersonSerializer
)
# from apps.technicalSupportData.api.models import ResponsibleData
# from apps.technicalSupportData.api.serializers import ResponsibleDataSerializer
from rest_framework.decorators import api_view

from .models import GeneralProcedure
from .serializers import GeneralProcedureSerializer

from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

@api_view(['GET'])
def get_data_all(resquest):
    if resquest.method == 'GET':
        data = GeneralProcedure.objects.all()
        data_serializer = GeneralProcedureSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def get_active(resquest):
    if resquest.method == 'GET':
        data = GeneralProcedure.objects.filter(active=True)
        data_serializer = GeneralProcedureSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['GET'])
def get_successfull_job(resquest):
    if resquest.method == 'GET':
        data = GeneralProcedure.objects.filter(successfull_job=True)
        data_serializer = GeneralProcedureSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

class SearchClientDataView(generics.ListAPIView):
    queryset = GeneralProcedure.objects.all()
    serializer_class = GeneralProcedureSerializer
    filter_backends = [SearchFilter]
    search_fields = (
        'client_data__mail',
        'client_data__telephone',
        'client_data__person_identification__dni',
        'client_data__person_identification__fisrt_name',
        'client_data__person_identification__second_name',
        'client_data__person_identification__father_surname',
        'client_data__person_identification__mother_surname',
        'client_data__person_identification__mobile',
    )

"""Create a new procedure"""
@api_view(['POST'])
def create_procedure(resquest):
    if resquest.method == 'POST':
        data = GeneralProcedureSerializer(data=resquest.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=201)
        return JsonResponse(data.errors, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['POST'])
def create_client_data(request):
    if request.method == 'POST':
        data = OwnerSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=201)
        return JsonResponse(data.errors, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['POST'])
def create_municipal_account(request):
    if request.method == 'POST':
        data = MunicipalAccountSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=201)
        return JsonResponse(data.errors, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['POST'])
def create_person(request):
    if request.method == 'POST':
        data = PersonSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=201)
        return JsonResponse(data.errors, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['POST'])
def create_houses_client(request):
    if request.method == 'POST':
        data = HousesClientSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=201)
        return JsonResponse(data.errors, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['POST'])
def cadastral(request):
    if request.method == 'POST':
        data = CadastralSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=201)
        return JsonResponse(data.errors, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

# @api_view(['POST'])
# def responsibles_data(request):
#     if request.method == 'POST':
#         data = ResponsibleDataSerializer(data=request.data)
#         if data.is_valid():
#             data.save()
#             return JsonResponse(data.data, status=201)
#         return JsonResponse(data.errors, status=400)

#     return JsonResponse({'error': 'Metodo no soportado'}, status=400)

"""Update and delete procedure"""
@api_view(['PUT', 'DELETE'])
def update_procedure(request, pk):
    try:
        data = GeneralProcedure.objects.get(pk=pk)
    except GeneralProcedure.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        data_serializer = GeneralProcedureSerializer(data, data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=201)
        return JsonResponse(data_serializer.errors, status=400)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=204)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['PUT', 'DELETE'])
def update_client_data(request, pk):
    try:
        data = OwnerData.objects.get(pk=pk)
    except OwnerData.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        data_serializer = OwnerSerializer(data, data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=201)
        return JsonResponse(data_serializer.errors, status=400)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=204)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['PUT', 'DELETE'])
def update_municipal_account(request, pk):
    try:
        data = MunicipalAccountData.objects.get(pk=pk)
    except MunicipalAccountData.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        data_serializer = MunicipalAccountSerializer(data, data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=201)
        return JsonResponse(data_serializer.errors, status=400)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=204)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['PUT', 'DELETE'])
def update_person(request, pk):
    try:
        data = PersonData.objects.get(pk=pk)
    except PersonData.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        data_serializer = PersonSerializer(data, data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=201)
        return JsonResponse(data_serializer.errors, status=400)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=204)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['PUT', 'DELETE'])
def update_houses_client(request, pk):
    try:
        data = HouseClientData.objects.get(pk=pk)
    except HouseClientData.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        data_serializer = HousesClientSerializer(data, data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=201)
        return JsonResponse(data_serializer.errors, status=400)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=204)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

@api_view(['PUT', 'DELETE'])
def update_cadastral(request, pk):
    try:
        data = CadastralData.objects.get(pk=pk)
    except CadastralData.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        data_serializer = CadastralSerializer(data, data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=201)
        return JsonResponse(data_serializer.errors, status=400)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=204)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)

# @api_view(['PUT', 'DELETE'])
# def update_responsibles_data(request, pk):
#     try:
#         data = ResponsibleData.objects.get(pk=pk)
#     except ResponsibleData.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'PUT':
#         data_serializer = ResponsibleDataSerializer(data, data=request.data)
#         if data_serializer.is_valid():
#             data_serializer.save()
#             return JsonResponse(data_serializer.data, status=201)
#         return JsonResponse(data_serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         data.delete()
#         return Response(status=204)
#     return JsonResponse({'error': 'Metodo no soportado'}, status=400)

