from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SaleCreateSerializer, SaleSer
from .models import SaleProduct

@api_view(['POST'])
def AddSale(request):
    ser = SaleCreateSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getByUser(request, id):
    data = SaleProduct.objects.filter(sale__customer__pk=id)
    ser = SaleSer(data, many=True)
    return Response(ser.data)
