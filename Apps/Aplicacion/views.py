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
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view



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
class ReactViewArticulo_list(APIView):
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

class ReactViewArticulo_detail(APIView):
# def get(self, request):
#         articulos = [{"idArticulo": articulos.idArticulo, "nombre": articulos.nombre, "descripcion": articulos.descripcion, "precio": articulos.precio, "color": articulos.color} for articulos in Articulo.objects.all()]
#         return Response(articulos, status=200)
    def get(self, request, idArticulo):
        try:
            articulopk = Articulo.objects.get(idArticulo=idArticulo)
        except Articulo.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ArticuloSerializer(articulopk)
        return Response(serializer.data, status=200)

    def put(self, request, idArticulo):
        try:
            articulopk = Articulo.objects.get(idArticulo=idArticulo)
        except Articulo.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ArticuloSerializer(articulopk, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

    def delete(self, request, idArticulo):
        try:
            articulopk = Articulo.objects.get(idArticulo=idArticulo)
        except Articulo.DoesNotExist:
            return HttpResponse(status=404)
        articulopk.delete()
        return HttpResponse(status=204)
    # @api_view(['GET', 'PUT', 'DELETE'])
    # def articulo_details(request, idArticulo):
    #     try:
    #         articulo = Articulo.objects.get(idArticulo=idArticulo)
    #     except Articulo.DoesNotExist:
    #         return HttpResponse(status=404)
    #     if request.method == 'GET':
    #         serializer = ArticuloSerializer(articulo)
    #         return JsonResponse(serializer.data)
    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = ArticuloSerializer(articulo, data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=400)
    #     elif request.method == 'DELETE':
    #         articulo.delete()
    #         return HttpResponse(status=204)

    # def put(self, request, idArticulo):
    #     blog = Articulo.objects.get(idArticulo=idArticulo)
    #     serializer = ArticuloSerializer(blog, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=200)
    #     else:
    #         return Response(serializer.errors, status=400)


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



















# from django.shortcuts import render
# from django.http.response import JsonResponse
# from django.views import View
# from .models import Articulo
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# import json
# # Create your views here.

# class ArticuloView(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get (self, request, idArticulo=0):
#         if (idArticulo>0):
#             articulos=list(Articulo.objects.filter(idArticulo=id).values())
#             if len(articulos)>0:
#                 articulo=articulos[0]
#                 datos={'mensaje':'Articulo encontrado','articulo':articulo}
#                 return JsonResponse(datos, safe=False, status=200)
#             else:
#                 datos={'mensaje':'Articulos no encontrados'}
#                 return JsonResponse(datos, safe=False, status=404)
#         else:
#             articulos=list(Articulo.objects.all().values())
#             if len(articulos)>0:
#                 datos={'mensaje':'Articulos encontrados','articulos':articulos}
#                 return JsonResponse(datos, safe=False, status=200)
#             else:
#                 datos={'mensaje':'Articulos no encontrados'}
#                 return JsonResponse(datos, safe=False, status=404)

    # def get(self, request, id=0):
    #     if (id>0):
    #         libros=list(Libro.objects.filter(id=id).values())
    #         if len(libros) > 0:
    #             libro=libros[0]
    #             datos={'message': "success",'libro':libro}
    #             return JsonResponse(datos)
    #         else:
    #             datos={'message': "Libros not found..."}
    #             return JsonResponse(datos)

    #     else:
    #         libros =list(Libro.objects.values())
    #         if len(libros)>0:
    #             datos={'message': "success",'Libros':libros}
    #         else:
    #             datos={'message': "Libros not found..."}
    #         return JsonResponse(datos)

    # def post(self, request):
    #     jd = json.loads(request.body)
    #     Libro.objects.create(tipoportada_id=jd['tipoportada_id'], nombre=jd['nombre'], descripcion=jd['descripcion'], autor=jd['autor'], editorial=jd['editorial'], alto=jd['alto'], ancho=jd['ancho'],largo=jd['largo'], idioma=jd['idioma'], precio=jd['precio'], numpaginas=jd['numpaginas'], categoria=jd['categoria'], descuento=jd['descuento'], unidades=jd['unidades'], estado=jd['estado'], imagen=jd['imagen'])
    #     datos={'message': "success"}
    #     return JsonResponse(datos)


    # def put(self, request, id):
    #     jd = json.loads(request.body)
    #     libros=list(Libro.objects.filter(id=id).values())
    #     if len(libros) > 0:
    #         libro=Libro.objects.get(id=id)
    #         libro.tipoportada_id=jd['tipoportada_id']
    #         libro.nombre=jd['nombre']
    #         libro.descripcion=jd['descripcion']
    #         libro.autor=jd['autor']
    #         libro.editorial=jd['editorial']
    #         libro.alto=jd['alto']
    #         libro.ancho=jd['ancho']
    #         libro.largo=jd['largo']
    #         libro.idioma=jd['idioma']
    #         libro.precio=jd['precio']
    #         libro.numpaginas=jd['numpaginas']
    #         libro.categoria=jd['categoria']
    #         libro.descuento=jd['descuento']
    #         libro.unidades=jd['unidades']
    #         libro.estado=jd['estado']
    #         libro.imagen=jd['imagen']
    #         libro.save()
    #         datos={'message': "success"}
    #         return JsonResponse(datos)
    #     else:
    #         datos={'message': "Libros not found..."}

    # def delete(self, request, id):
    #     libros=list(Libro.objects.filter(id=id).values())
    #     if len(libros) > 0:
    #         Libro.objects.filter(id=id).delete()
    #         datos={'message': "success"}
    #     else:
    #         datos={'message': "Libros not found..."}
    #     return JsonResponse(datos)
