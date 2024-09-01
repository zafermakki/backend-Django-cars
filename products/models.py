from django.db import models

class Category(models.Model):
    name= models.CharField(max_length= 250, unique= True)
    image_path= models.ImageField(upload_to= 'categories/')
    
    class Meta:
        db_table= 'categories'
        
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name= models.CharField(max_length= 250)
    category= models.ForeignKey(Category, on_delete= models.DO_NOTHING)
    description=models.TextField(default= "", blank= True)
    price= models.DecimalField(max_digits= 20, decimal_places=4)
    image_path= models.ImageField(upload_to= 'categories/')
    video_url = models.URLField(max_length=200, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    
    class Meta:
        db_table= 'products'
        
    def __str__(self) -> str:
        return self.name + ' ' + self.category.name
