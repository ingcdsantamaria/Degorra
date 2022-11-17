

import React from "react";
import '../stylesheets/FeaturedProducts.css'


function FeaturedProducts(props) {
    return (
        <div className="contenedor-producto">
            <a href="Producto.jsx">
                <img className="imagen-producto" src={require(`../images/imagen-productoDestacado-gorra-${props.imagen}.png`)} alt="Producto destacado" />
            </a>
            <div className="contenedor-descripcion">
                <a href="Producto.jsx">
                    <h3 className="descripcion-tittle">{props.titulo}</h3>
                </a>
                <p className="descripcion-precio">$ {props.precio}</p>
                </div>
        </div>
    );
}

export default FeaturedProducts;