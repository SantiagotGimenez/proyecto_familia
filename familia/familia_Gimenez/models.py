from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=20)
    parentesco = models.CharField(max_length=20)
    edad = models.IntegerField()
    cumpleanios = models.DateField()

    def __str__(self):
        return self.nombre
    def __str__(self):
        return self.parentesco
    
   
