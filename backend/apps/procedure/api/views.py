from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from .models import GeneralProcedure
from .serializers import GeneralProcedureSerializer

@api_view(['GET'])
def getDataAll(resquest):
    if resquest.method == 'GET':
        data = GeneralProcedure.objects.all()
        data_serializer = GeneralProcedureSerializer(data,many=True)
        return JsonResponse(data_serializer.data, safe=False)
