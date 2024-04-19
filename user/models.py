from django.db import models

# Create your models here.
class occasion(models.Model):
    occasionType = models.CharField(max_length=50)
    description = models.CharField( max_length=50)
    