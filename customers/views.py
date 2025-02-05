from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Customer
from .serializers import CustomerModelSerializer



@api_view(['POST'])
def checkUser(request):
    data = request.data
    client= Customer.objects.filter(username= data['username'], 
                                  password= data['password']).first()
    if client is not None:
        serializer = CustomerModelSerializer(client)
        return Response(serializer.data, status= status.HTTP_200_OK)
    return Response({}, status= status.HTTP_404_NOT_FOUND)  

@api_view(['POST'])
def addUser(request):
    data= request.data
    serializer= CustomerModelSerializer(data= data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

