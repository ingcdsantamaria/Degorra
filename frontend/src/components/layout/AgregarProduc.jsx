import React from 'react'
//import agregarIcon from '@mui/icons-material/agregar';
import CleanHandsIcon from '@mui/icons-material/CleanHands';
import SaveAsIcon from '@mui/icons-material/SaveAs';
import '../stylesheets/AgregarProduc.css';
import { useDispatch } from 'react-redux';
import { createArticulo } from '../../redux/slices/articulos';
// import { addArticulos } from '../../redux/slices/articulos';
// import { useDispatch, useSelector } from 'react-redux';
//import { Icon } from '@mui/material';

function AgregarProduc() {
    const [addArticulo, setAddArticulos] = React.useState({
        nombre: '',
        descripcion: '',
        precio: '',
        color: '',
    });
    const dispatch = useDispatch();

    const handleChange = (e) => {
        setAddArticulos({
            ...addArticulo,
            [e.target.name]: e.target.value,
        });
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        dispatch(createArticulo(addArticulo));
    }

    // const para limpiar los campos
    const limpiar = () => {
        document.getElementById("formulario").reset();
    }
    // const {list: articulos} = useSelector(state => state.articulos);
    // const dispatch = useDispatch();
    // const [articulochange, setArticulochange] = useState(articulos);
    // useEffect(() => {
    //     dispatch(fetchAllArticulos());
    //     setArticulochange(articulos);
    // }, [dispatch, articulos]);

    return (
        <>
            <div className="contenedor-admin-derec">
                <div className="contenedor-admin-derec-tittle">
                    <h1 className='tittle-agregar' >agregar Producto</h1>
                </div>
                <div className="contenedor-admin-derec-form">
                    <form onSubmit={handleSubmit} id="formulario" >
                        <div className="contenedor-admin-derec-form-agregar-imagen">
                            <div className="contenedor-admin-derec-form-agregar-imagen-input">
                                <input type="file" name="imagen" id="imagen" />
                                <input type="submit" value="subir" className='btn'  />
                            </div>
                        </div>
                        <div className="contenedor-admin-derec-form-agregar-titulo">
                            <div className="contenedor-admin-derec-form-agregar-titulo-input">
                                <input type="text" name="nombre" id="titulo" placeholder="Titulo del producto" onChange={handleChange} />
                            </div>
                        </div>
                        <div className="contenedor-admin-derec-form-agregar-descripcion">
                            <div className="contenedor-admin-derec-form-agregar-descripcion-textarea">
                                <textarea name="descripcion" id="descripcion" cols="30" rows="10" placeholder="Descripcion del producto" onChange={handleChange} ></textarea>
                            </div>
                        </div>
                        <div className="contenedor-admin-derec-form-agregar-color">
                            <div className="contenedor-admin-derec-form-agregar-color-input">
                                <input type="text" name="color" id="color" placeholder="color del producto" onChange={handleChange} />
                            </div>
                        </div>
                        <div className="contenedor-admin-derec-form-agregar-catetoria">
                            <div className="contenedor-admin-derec-form-agregar-catetoria-select">
                                <select name="categoria" id="categoria"  onChange={handleChange} >
                                <option value="Default" disabled>Seleccione un campo</option>
                                    <option value="hombres">Hombres</option>
                                    <option value="mujeres">Mujeres</option>
                                    <option value="ninos">Niños</option>
                                    <option value="accesorios">Accesorios</option>
                                </select>
                            </div>
                        </div>
                        <div className="contenedor-admin-derec-form-agregar-precio">
                            <div className="contenedor-admin-derec-form-agregar-precio-input">
                                <input type="number" name="precio" id="precio" placeholder="Precio del producto" min={10000}  onChange={handleChange}/>
                            </div>
                        </div>
                        <div className="contenedor-admin-derec-form-botones">
                            <div className="contenedor-admin-derec-form-botones-guardar-cancelar">
                                <button type="submit" className="btn-guardar" onClick={handleSubmit} ><SaveAsIcon />Guardar</button>
                                <button type='button' className="btn-cancelar" onClick={limpiar} ><CleanHandsIcon />Limpiar</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </>
    );
}

export default AgregarProduc;