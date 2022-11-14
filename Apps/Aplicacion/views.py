#importamos el modelo django.shortcuts import render que nos permite renderizar una plantilla
from django.shortcuts import render
#importamos el modelo de django.http import HttpResponse que nos permite retornar una respuesta http al cliente
from django.http import HttpResponse
#importamos el modelo de django.http import JsonResponse que nos permite retornar una respuesta http al cliente en formato json
from django.http import JsonResponse
#importamos el modelo de rest_framework.views import APIView que nos permite crear una vista basada en clases
from rest_framework.views import APIView
#importamos el modelo de rest_framework.response import Response que nos permite retornar una respuesta http al cliente en formato json
from rest_framework.response import Response
#importamos el modelo de .models import UsuarioCliente que nos permite importar el modelo de la base de datos
from .models import *
from .serializer import *



# Create your views here.
#se creara una clase que hereda de APIView para poder crear una vista basada en clases
class ReactViewUsuarioCliente(APIView):
    #se crea un metodo get que recibe como parametro self para poder hacer referencia a la clase y request para poder recibir los datos del cliente
    def get(self, request):
        #se crea una variable que tendra todos los datos de la base de datos de la tabla UsuarioCliente con un for que recorre todos los datos de la base de datos
        usuariosClientes = [{"idUsuarioCliente": usuariosClientes.idUsuarioCliente, "nombre": usuariosClientes.nombre, "apellido": usuariosClientes.apellido, "correo": usuariosClientes.correo, "contraseña": usuariosClientes.contraseña, "rol": usuariosClientes.rol, "codigo": usuariosClientes.codigo} for usuariosClientes in UsuarioCliente.objects.all()]
        return Response(usuariosClientes, status=200)
    def post(self, request):
        #se crea una variable que tendra todos los datos serializados de la tabla UsuarioCliente
        serializer = UsuarioClienteSerializer(data=request.data)
        #se valida si los datos son correctos
        if serializer.is_valid(raise_exception=True):
            #se guarda los datos en la base de datos
            serializer.save()
            #se retorna una respuesta http al cliente en formato json con el codigo 201 que significa que la peticion fue exitosa y con los datos de la base de datos
            return Response(serializer.data, status=201)

#se creara una clase que hereda de APIView para poder crear una vista basada en clases
class ReactViewUsuarioAdmin(APIView):
    #se crea un metodo get que recibe como parametro self para poder hacer referencia a la clase y request para poder recibir los datos del cliente
    def get(self, request):
        #se crea una variable que tendra todos los datos de la base de datos de la tabla UsuarioAdmin con un for que recorre todos los datos de la base de datos
        usuariosAdmins = [{"idUsuarioAdmin": usuariosAdmins.idUsuarioAdmin, "nombre": usuariosAdmins.nombre, "apellido": usuariosAdmins.apellido, "correo": usuariosAdmins.correo, "contraseña": usuariosAdmins.contraseña, "rol": usuariosAdmins.rol} for usuariosAdmins in UsuarioAdmin.objects.all()]
        #se retorna una respuesta http al cliente en formato json con el codigo 200 que significa que la peticion fue exitosa y con los datos de la base de datos
        return Response(usuariosAdmins, status=200)

    #se crea un metodo post que recibe como parametro self para poder hacer referencia a la clase y request para poder recibir los datos del cliente
    def post(self, request):
        #se crea una variable que tendra todos los datos serializados de la tabla UsuarioAdmin
        serializer = UsuarioAdminSerializer(data=request.data)
        #se valida si los datos son correctos
        if serializer.is_valid(raise_exception=True):
            #se guarda los datos en la base de datos
            serializer.save()
            #se retorna una respuesta http al cliente en formato json con el codigo 201 que significa que la peticion fue exitosa y con los datos de la base de datos
            return Response(serializer.data, status=201)

#se creara una clase que hereda de APIView para poder crear una vista basada en clases
class ReactViewArticulo(APIView):
    #se crea un metodo get que recibe como parametro self para poder hacer referencia a la clase y request para poder recibir los datos del cliente
    def get(self, request):
        #se crea una variable que tendra todos los datos de la base de datos de la tabla Articulo con un for que recorre todos los datos de la base de datos
        articulos = [{"idArticulo": articulos.idArticulo, "nombre": articulos.nombre, "descripcion": articulos.descripcion, "precio": articulos.precio, "color": articulos.color} for articulos in Articulo.objects.all()]
        #se retorna una respuesta http al cliente en formato json con el codigo 200 que significa que la peticion fue exitosa y con los datos de la base de datos
        return Response(articulos, status=200)

    #se crea un metodo post que recibe como parametro self para poder hacer referencia a la clase y request para poder recibir los datos del cliente
    def post(self, request):
        #se crea una variable que tendra todos los datos serializados de la tabla Articulo
        serializer = ArticuloSerializer(data=request.data)
        #se valida si los datos son correctos
        if serializer.is_valid(raise_exception=True):
            #se guarda los datos en la base de datos
            serializer.save()
            #se retorna una respuesta http al cliente en formato json con el codigo 201 que significa que la peticion fue exitosa y con los datos de la base de datos
            return Response(serializer.data, status=201)


#se creara una clase que hereda de APIView para poder crear una vista basada en clases
class ReactViewInventario(APIView):
    #se crea un metodo get que recibe como parametro self para poder hacer referencia a la clase y request para poder recibir los datos del cliente
    def get(self, request):
        #se crea una variable que tendra todos los datos de la base de datos de la tabla Inventario con un for que recorre todos los datos de la base de datos
        inventarios = [{"idInventario": inventarios.idInventario, "idArticulo": inventarios.idArticulo, "idUsuarioAdmin": inventarios.idUsuarioAdmin} for inventarios in Inventario.objects.all()]
        #se retorna una respuesta http al cliente en formato json con el codigo 200 que significa que la peticion fue exitosa y con los datos de la base de datos
        return Response(inventarios, status=200)
    #se crea un metodo post que recibe como parametro self para poder hacer referencia a la clase y request para poder recibir los datos del cliente
    def post(self, request):
        #se crea una variable que tendra todos los datos serializados de la tabla Inventario
        serializer = InventarioSerializer(data=request.data)
        #se valida si los datos son correctos
        if serializer.is_valid(raise_exception=True):
            #se guarda los datos en la base de datos
            serializer.save()
            #se retorna una respuesta http al cliente en formato json con el codigo 201 que significa que la peticion fue exitosa y con los datos de la base de datos
            return Response(serializer.data, status=201)


#se creara una clase que hereda de APIView para poder crear una vista basada en clases
class ReactViewCarritoCompra(APIView):
    def get(self, request):
        #se crea una variable que tendra todos los datos de la base de datos de la tabla CarritoCompra con un for que recorre todos los datos de la base de datos
        carritosCompras = [{"idCarritoCompra": carritosCompras.idCarritoCompra, "idArticulo": carritosCompras.idArticulo, "cantidad": carritosCompras.cantidad, "precioTotal": carritosCompras.precioTotal} for carritosCompras in CarritoCompra.objects.all()]
        #se retorna una respuesta http al cliente en formato json con el codigo 200 que significa que la peticion fue exitosa y con los datos de la base de datos
        return Response(carritosCompras, status=200)
    #se crea un metodo post que recibe como parametro self para poder hacer referencia a la clase y request para poder recibir los datos del cliente
    def post(self, request):
        #se crea una variable que tendra todos los datos serializados de la tabla CarritoCompra
        serializer = CarritoCompraSerializer(data=request.data)
        #se valida si los datos son correctos
        if serializer.is_valid(raise_exception=True):
            #se guarda los datos en la base de datos
            serializer.save()
            #se retorna una respuesta http al cliente en formato json con el codigo 201 que significa que la peticion fue exitosa y con los datos de la base de datos
            return Response(serializer.data, status=201)


#se creara una clase que hereda de APIView para poder crear una vista basada en clases
class ReactViewFacturacion(APIView):
    def get(self, request):
        #se crea una variable que tendra todos los datos de la base de datos de la tabla Facturacion con un for que recorre todos los datos de la base de datos
        facturaciones = [{"idFacturacion": facturaciones.idFacturacion, "idCarritoCompra": facturaciones.idCarritoCompra, "fecha": facturaciones.fecha, "precioFinal": facturaciones.precioFinal} for facturaciones in Facturacion.objects.all()]
        #se retorna una respuesta http al cliente en formato json con el codigo 200 que significa que la peticion fue exitosa y con los datos de la base de datos
        return Response(facturaciones, status=200)
    #se crea un metodo post que recibe como parametro self para poder hacer referencia a la clase y request para poder recibir los datos del cliente
    def post(self, request):
        #se crea una variable que tendra todos los datos serializados de la tabla Facturacion
        serializer = FacturacionSerializer(data=request.data)
        #se valida si los datos son correctos
        if serializer.is_valid(raise_exception=True):
            #se guarda los datos en la base de datos
            serializer.save()
            #se retorna una respuesta http al cliente en formato json con el codigo 201 que significa que la peticion fue exitosa y con los datos de la base de datos
            return Response(serializer.data, status=201)