import React from 'react';
import EditProduct from './EditProduct';
import AgregarProduc from './AgregarProduc';
import '../stylesheets/AdminDerec.css'

function AdminDerec(props) {
    const newProduct = props.change;
    const EditProducto = props.new;
    if(newProduct){
        return <AgregarProduc addArticulo={props.addArticulo} setAddArticulo={props.setAddArticulo} />
    }else if(EditProducto){
        return <EditProduct articuloSeleccionado={props.articulo} />
    }else{
        return (
            <>
                <div className="contenedor-admin-der-producto">
                    <h1>Seleccione un producto para editarlo o precione el boton de agregar producto</h1>
                </div>
            </>
        );
        // return (
        //     <>
        //         <div>
        //             {/* {props.change ? <EditProduct /> : <AgregarProduc />}*/}
        //             {props.change? <AgregarProduc /> : <h1>Seleccione un producto para editarlo o precione el boton de agregar producto</h1>}
        //             {props.new? <EditProduct /> : <h1>Seleccione un producto para editarlo o precione el boton de agregar producto</h1>}
        //         </div>
        //     </>
        //     );
}}


export default AdminDerec;