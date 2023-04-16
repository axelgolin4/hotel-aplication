from django.db import models

class Insumos(models.Model):    
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    carne = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
