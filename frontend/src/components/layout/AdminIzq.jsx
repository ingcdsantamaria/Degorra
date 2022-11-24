import React, { useEffect } from 'react'
import AddIcon from '@mui/icons-material/Add';
import AdminProducto from './AdminProducto'
import '../stylesheets/AdminIzq.css'
import { fetchAllArticulos } from '../../redux/slices/articulos';
import { useDispatch } from 'react-redux';



export default function AdminIzq(props) {
    // const articulosList = useSelector(state => state.articulos.value);
    const dispatch = useDispatch();
    // const [articulochange, setArticulochange] = useState(articulos);
    useEffect(() => {
        dispatch(fetchAllArticulos());
    }, [dispatch]);
    
    return (
        <>
        <header>
            <div className="contenedor-admin-izq-header">
                <div className="contenedor-admin-izq-tittle">
                    <div className="admin-izq">
                        <button onClick={props.onChange} id="bool"><AddIcon />Agregar</button>
                    </div>
                </div>
            </div>
        </header>
        <main>
            <div className="contenedor-admin-izq">
                {props.articulosList.map(function (articulo, index) {
                    return (
                        <div key={index} onClick={() => props.setArticulo(articulo)}>
                        <AdminProducto
                        key={articulo.id}
                        imagen="adidas-gris"
                        inchange={props.inchange}
                        nombre={articulo.nombre}
                        descripcion={articulo.descripcion}
                        precio={articulo.precio}
                        color={articulo.color}
                        />
                        </div>
                    )
                })}
            </div>
        </main>
        </>
    );
}
