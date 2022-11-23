from django.db import models
from .choices import *
# Create your models here.
class UsuarioCliente (models.Model):
    idUsuarioCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, verbose_name='nombres')
    apellido = models.CharField(max_length=30, verbose_name='apellidos')
    correo = models.EmailField(verbose_name='correo')
    contraseña = models.CharField(max_length=15, verbose_name='contraseña')
    rol = models.CharField(max_length=30, choices=rol, default='cliente', verbose_name='rol')
    codigo = models.IntegerField(verbose_name='codigo',blank=True,null=True)

    
    def nombre_completo(self):
        return "{} {}".format(self.nombre, self.apellido)
    
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name = 'UsuarioCliente'
        verbose_name_plural = 'UsuarioClientes'
        db_table='UsuarioCliente'
        ordering = ['idUsuarioCliente']
    
class UsuarioAdmin (models.Model):
    idUsuarioAdmin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, verbose_name='nombres')
    apellido = models.CharField(max_length=30, verbose_name='apellidos')
    correo = models.EmailField(verbose_name='correo')
    contraseña = models.CharField(max_length=15, verbose_name='contraseña')
    rol = models.CharField(max_length=30, choices=rol, default='administrador', verbose_name='rol')
    
    def nombre_completo(self):
        return "{} {}".format(self.nombre, self.apellido)
    
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name = 'UsuarioAdmin'
        verbose_name_plural = 'UsuarioAdmins'
        db_table='UsuarioAdmin'
        ordering = ['idUsuarioAdmin']
        
class Articulo (models.Model):
    idArticulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, verbose_name='nombre')
    descripcion = models.CharField(max_length=100, verbose_name='descripcion')
    precio = models.IntegerField(verbose_name='precio')
    color = models.CharField(max_length=30, verbose_name='color')
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        db_table='Articulo'
        ordering = ['idArticulo']
        
class Inventario (models.Model):
    idInventario = models.AutoField(primary_key=True)
    idArticulo = models.ForeignKey(Articulo, null=True, blank=True, on_delete=models.CASCADE)
    idUsuarioAdmin = models.ForeignKey(UsuarioAdmin, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.idArticulo
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table='Inventario'
        ordering = ['idInventario']

        
class CarritoCompra (models.Model):
    idCarritoCompra = models.AutoField(primary_key=True)
    idUsuarioCliente = models.ForeignKey(UsuarioCliente, null=True, blank=True, on_delete=models.CASCADE)
    idArticulo = models.ForeignKey(Articulo, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='cantidad')
    precioTotal = models.IntegerField(verbose_name='precioTotal')
    
    def __str__(self):
        return self.idUsuarioCliente
    
    class Meta:
        verbose_name = 'CarritoCompra'
        verbose_name_plural = 'CarritoCompras'
        db_table='CarritoCompra'
        ordering = ['idCarritoCompra']
    
class Facturacion(models.Model):
    idFacturacion = models.AutoField(primary_key=True)
    idCarritoCompra = models.ForeignKey(CarritoCompra, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True, verbose_name='fecha')
    precioFinal = models.IntegerField(verbose_name='precioFinal')
    
    def __str__(self):
        return self.idCarritoCompra
    
    class Meta:
        verbose_name = 'Facturacion'
        verbose_name_plural = 'Facturacions'
        db_table='Facturacion'
        ordering = ['idFacturacion']