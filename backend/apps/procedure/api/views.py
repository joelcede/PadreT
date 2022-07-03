from django.http.response import JsonResponse
from apps.clientData.api.serializers import PersonSerializer
from rest_framework.decorators import api_view

from .models import GeneralProcedure
from .serializers import GeneralProcedureSerializer
from ...clientData.api.models import Person

from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from ...clientData.api.filters import PersonFilter
#from rest_framework.view.generic import ListAPIView

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

class PersonView(generics.ListAPIView):
    queryset = GeneralProcedure.objects.all()
    serializer_class = GeneralProcedureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'client_data__person_identification__dni': ['contains'],
    }

@api_view(['GET'])
def get_data_dni(resquest):
    if resquest.method == 'GET':
        person = Person.objects.all()
        person_filter = PersonFilter(resquest.GET, queryset=person)
        data_serializer = PersonSerializer(person_filter, many=True)
        return JsonResponse(data_serializer.data, safe=False)
    return JsonResponse({'error': 'Metodo no soportado'}, status=400)