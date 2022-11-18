#se importara rest_framework para poder usar los serializadores esto es para poder convertir los datos de la base de datos a json
from rest_framework import serializers
#se importara el modelo de la base de datos
from .models import *

#se creara una clase que hereda de serializers.ModelSerializer para poder convertir los datos de la base de datos a json
class UsuarioClienteSerializer(serializers.ModelSerializer):
    #se creara una clase meta que tendra el modelo que se va a serializar y los campos que se van a mostrar
    class Meta:
        model = UsuarioCliente
        #se creara un campo que tendra todos los campos del modelo
        fields = '__all__'

#se creara una clase que hereda de serializers.ModelSerializer para poder convertir los datos de la base de datos a json
class UsuarioAdminSerializer(serializers.ModelSerializer):
    #se creara una clase meta que tendra el modelo que se va a serializar y los campos que se van a mostrar
    class Meta:
        model = UsuarioAdmin
        #se creara un campo que tendra todos los campos del modelo
        fields = '__all__'

#se creara una clase que hereda de serializers.ModelSerializer para poder convertir los datos de la base de datos a json
class ArticuloSerializer(serializers.ModelSerializer):
    #se creara una clase meta que tendra el modelo que se va a serializar y los campos que se van a mostrar
    class Meta:
        model = Articulo
        #se creara un campo que tendra todos los campos del modelo
        fields = ['idArticulo', 'nombre', 'descripcion', 'precio', 'color']

#se creara una clase que hereda de serializers.ModelSerializer para poder convertir los datos de la base de datos a json
class InventarioSerializer(serializers.ModelSerializer):
    #se creara una clase meta que tendra el modelo que se va a serializar y los campos que se van a mostrar
    class Meta:
        model = Inventario
        #se creara un campo que tendra todos los campos del modelo
        fields = '__all__'

#se creara una clase que hereda de serializers.ModelSerializer para poder convertir los datos de la base de datos a json
class CarritoCompraSerializer(serializers.ModelSerializer):
    #se creara una clase meta que tendra el modelo que se va a serializar y los campos que se van a mostrar
    class Meta:
        model = CarritoCompra
        #se creara un campo que tendra todos los campos del modelo
        fields = '__all__'

#se creara una clase que hereda de serializers.ModelSerializer para poder convertir los datos de la base de datos a json
class FacturacionSerializer(serializers.ModelSerializer):
    #se creara una clase meta que tendra el modelo que se va a serializar y los campos que se van a mostrar
    class Meta:
        model = Facturacion
        #se creara un campo que tendra todos los campos del modelo
        fields = '__all__'