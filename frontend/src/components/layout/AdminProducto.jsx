import React from 'react'
import DragHandleIcon from '@mui/icons-material/DragHandle';
import '../stylesheets/AdminProducto.css'

function AdminProducto(props) {
    return (
        <>
            <div className="contenedor-admin-izq-producto">
                <button onClick={props.inchange} className="contenedor-admin-izq-producto-drag">
                    <div className="contenedor-items-productos">
                        <div className="admin-izq-icono-producto">
                            <DragHandleIcon />
                        </div>
                        <div className="admin-izq-img-div">
                            <img className="admin-izq-img" src={require(`../images/gorra-${props.imagen}.png`)} alt="productos" />
                        </div>
                        <div className="admin-izq-tittle-div">
                            <h2 className="admin-izq-tittle">{props.nombre}</h2>
                            <p className="admin-izq-descripcion">{props.descripcion}</p>
                        </div>
                        <div className="admin-izq-precio-producto">
                            <p className="admin-izq-precio">$ {props.precio}</p>
                        </div>
                    </div>
                </button>
            </div>
        </>
    );
}

export default AdminProducto;