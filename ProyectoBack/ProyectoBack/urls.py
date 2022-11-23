"""ProyectoBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Apps.Aplicacion.views import *
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReactViewUsuarioCliente.as_view()),
    path('usuario/', ReactViewUsuarioAdmin.as_view(), name='usuario'),
    path('articulo/', ReactViewArticulo_list.as_view(), name='articulo'),
    path('articulo/<int:idArticulo>/', ReactViewArticulo_detail.as_view()),
    path('inventario/', ReactViewInventario.as_view(), name='inventario'),
    path('carrito/', ReactViewCarritoCompra.as_view(), name='carrito'),
    path('facturacion/', ReactViewFacturacion.as_view(), name='facturacion'),
]
# from django.contrib import admin
# from django.urls import path, include

# #se importa el archivo dejango.conf.urls para poder usar la funcion include que permite incluir las urls de otras aplicaciones
# from django.urls import re_path as url
# #from django.conf.urls import url
# #se importa el archivo aplicaion.views para poder usar las vistas de la aplicacion
# from Apps.Aplicacion.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #path('api/', include('Apps.Aplicacion.urls')),
# ]
