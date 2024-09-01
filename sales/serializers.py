from rest_framework import serializers
from .models import Sale, SaleProduct, Product
from customers.models import Customer

class SaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = '__all__'
        
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class SaleProductsCreateSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField()

class SaleCreateSerializer(serializers.Serializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    products = SaleProductsCreateSerializer(write_only=True, many=True)

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        customer = validated_data['customer']
        
        # Step 1: Validate product availability without modifying the database
        for product_data in products_data:
            product = product_data['id']
            quantity = product_data['quantity']

            # Check if the product quantity is available
            if product.quantity < quantity:
                raise serializers.ValidationError({
                    "quantity": f"Not enough quantity for {product.name}. Available: {product.quantity}."
                })

        # Step 2: If all products have sufficient quantity, create the Sale instance
        sale = Sale.objects.create(customer=customer)

        # Step 3: Proceed to decrease the stock and create SaleProduct entries
        for product_data in products_data:
            product = product_data['id']
            quantity = product_data['quantity']

            # Reduce the product quantity in stock
            product.quantity -= quantity
            product.save()

            # Create SaleProduct entry
            SaleProduct.objects.create(product=product, sale=sale, quantity=quantity)

        return sale


class SaleSer(serializers.Serializer):
    name = serializers.CharField(max_length=250, source='product.name')
    category = serializers.CharField(max_length=250, source='product.category.name')
    price = serializers.DecimalField(max_digits=20, decimal_places=4, source='product.price')
    image_path = serializers.CharField(max_length=250, source='product.image_path')
    quantity = serializers.IntegerField()
