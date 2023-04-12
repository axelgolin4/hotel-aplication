from django.db import models

class Cocina(models.Model):  
    id = models.AutoField(primary_key=True)  
    producto = models.CharField(max_length=200)
    proveedor = models.CharField(max_length=200)
    subcategoria = models.CharField(max_length=200)
    stock = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return self.producto

class Insumos(models.Model):    
    id = models.AutoField(primary_key=True)  
    producto = models.CharField(max_length=200)
    proveedor = models.CharField(max_length=200)
    subcategoria = models.CharField(max_length=200)
    stock = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return self.producto

class Blancos(models.Model):   
    id = models.AutoField(primary_key=True)   
    producto = models.CharField(max_length=200)
    proveedor = models.CharField(max_length=200)
    subcategoria = models.CharField(max_length=200)
    stock = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return self.producto