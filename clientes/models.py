from datetime import datetime
from django.db import models
from productos.models import Producto

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=60,blank=False)
    apellido=models.CharField(max_length=60,blank=False)
    telefono=models.CharField(max_length=20,blank=False)
    nit=models.CharField(max_length=20,blank=True)
    correo=models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    fecha_registro=models.DateTimeField(default = datetime.now, blank = True)


    def __str__(self):
        return f'{self.cliente},  compro: {self.producto}'


