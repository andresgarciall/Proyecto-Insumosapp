from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria=models.CharField(max_length=80,blank=True)

    def __str__(self):
        return self.categoria

class Proveedor(models.Model):
    nombre=models.CharField(max_length=120,blank=True,verbose_name='nombre de la empresa')
    direccion=models.CharField(max_length=150,blank=True,verbose_name='direccion de la empresa')
    correo=models.EmailField(max_length=100,blank=True)
    nit=models.CharField(max_length=20,blank=True)
    telefono=models.CharField(max_length=20,blank=True)
    ciudad=models.CharField(max_length=50,blank=True)

    class Meta:
        verbose_name='Proveedor'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre=models.CharField(max_length=150,blank=True)
    marca=models.CharField(max_length=100,blank=True)
    precio=models.IntegerField(default=0,blank=True)
    imagen=models.ImageField(blank=True)
    cantidad=models.IntegerField(default=0,blank=True)
    sku=models.CharField(max_length=20,blank=True,verbose_name='referencia del producto')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    activo=models.BooleanField(default=False,verbose_name='¿esta activo?')


    def __str__(self):
        return self.nombre


