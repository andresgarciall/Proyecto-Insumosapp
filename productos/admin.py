from django.contrib import admin

from productos.models import Categoria, Producto, Proveedor

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)