from django.db import models

# Create your models here.

class vendor(models.Model):
    customerType = models.CharField( max_length=50)
    vendorname  = models.CharField( max_length=50)
    description =models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    def __str__(self): 
        return self.vendorname
    
class services(models.Model):
    vendorname = models.CharField( max_length=50)
    serviceName = models.CharField(max_length=50)
    rate = models.IntegerField()
    description = models.CharField( max_length=50) 
    image = models.ImageField( upload_to='static', height_field=None, width_field=None, max_length=None)
    def __str__(self): 
        return self.vendorname


