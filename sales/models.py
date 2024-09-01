from django.db import models
from customers.models import Customer
from products.models import Product

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sales"
        
    def __str__(self) -> str:
        return self.customer.username

class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)  # New field to store the quantity of each product

    class Meta:
        db_table = "sales_products"
        
    def __str__(self) -> str:
        return f'{self.sale.customer.username} - {self.product.name} - {self.quantity}'
