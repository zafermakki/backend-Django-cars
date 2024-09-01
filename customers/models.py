from django.db import models

class Customer(models.Model):
    username= models.CharField(max_length= 250, unique= True)
    password= models.CharField(max_length= 250)
    first_name= models.CharField(max_length= 250)
    last_name= models.CharField(max_length= 250)
    
    
    class Meta:
        db_table= 'customers'
        
    def __str__(self) -> str:
        return self.username