# Degorra
Tienda virtual de venta de gorras


### Problematica:

- Las labores repetitivas que no son sistematizadas en un establecimiento suelen demandar más tiempo, comprometen la calidad del servicio y pueden generar inconformidad en los clientes. La ausencia de un sistema eficiente para automatizar los pedidos y controlar el inventario para los insumos utilizados en la venta de sus productos en los establecimientos de ropa afecta su eficacia para atender a sus clientes.


### Diagrama de Contexto:

- EL siguiente diagrama definira los límites entre el sistema DeGorra y su ambiente, mostrando las entidades que interactúan con él:

```mermaid
graph TD;
    DeGorra-->Cliente;
    DeGorra-->Administrador;
    DeGorra-->Proveedores;
    DeGorra-->Visa;
    DeGorra-->Mastercard
```



### Diagrama de Entidad de Relaciones: 

Un diagrama entidad-relación, también conocido como modelo entidad relación o ERD, es un tipo de diagrama de flujo que ilustra cómo las "entidades", como personas, objetos o conceptos, se relacionan entre sí dentro de un sistema. Los diagramas ER se usan a menudo para diseñar o depurar bases de datos relacionales en los campos de ingeniería de software, sistemas de información empresarial, educación e investigación.

```mermaid
%%{init: {'theme':'darkMode'}}%%

erDiagram
    Usuario_Cliente ||--|{ Carrito_Compra : Tiene
    Usuario_Cliente{
      int UsuarioCliente_Id
      String Nombre
      String Apellido
      String Correo
      String Contrasena
      String Rol
    }
    Carrito_Compra ||--|{Articulo : Contiene
    Carrito_Compra{
        int UsuarioCliente_Id
        int Articulo_Id
        int Precio_Total
        int Cantidad
    }
    Articulo }|--||Inventario : Esta
    Articulo{
      int Articulo_Id
      file Imagen
      String Nombre
      String Descripcion
      int Precio
      String Color
      String Categoria
    }
    Inventario ||--|| Usuario_Admin : Administra
    Inventario{
      int Articulo_Id
      int UsuarioAdmin_Id
    }
    Usuario_Admin{
      int UsuarioAdmin_Id
      String Nombre
      String Apellido
      String Correo
      String Contrasena
      String Rol
    }
    Facturacion ||--||Carrito_Compra : Genera
    Facturacion{
      int No_orden
      int Articulo_Id
      int UsuarioCliente_Id
      int Precio_Total
      date Fecha
    }
```

### Diagrama de Casos de Uso: 
Requerimiento Funcional 1(RF_001): 


```mermaid
flowchart LR
  A(["Usuario Admin"])
  B(["Iniciar Sesion"])
  C(["Validar Credenciales"])
  A-->B
  B--"<<include>>"-->C
```
