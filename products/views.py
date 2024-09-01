from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Category, Product
from .serializers import CategoryModelSerializer, ProductModelSerializer

@api_view(['GET'])
def getCategories(request):
    categories= Category.objects.all()
    ser = CategoryModelSerializer(categories, many= True)
    return Response(data= ser.data, status= status.HTTP_200_OK)

@api_view(['GET'])
def getProductsByCatId(request, id):
    products = Product.objects.filter(category= id)
    ser= ProductModelSerializer(products, many= True)
    return Response(ser.data, status= status.HTTP_200_OK)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    ser= ProductModelSerializer(products, many= True)
    return Response(ser.data, status= status.HTTP_200_OK)

