from rest_framework import serializers
from .models import Product, Category

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'
        
class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'