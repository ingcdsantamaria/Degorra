from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UsuarioCliente)
admin.site.register(UsuarioAdmin)
admin.site.register(Articulo)
admin.site.register(Inventario)
admin.site.register(CarritoCompra)
admin.site.register(Facturacion)