
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import SaveAsIcon from '@mui/icons-material/SaveAs';
import '../stylesheets/EditProduc.css';
import { editArticulo } from '../../redux/slices/articulos';
import { removeArticulo } from '../../redux/slices/articulos';
import { addArticulo } from '../../redux/slices/articulos';
import { useDispatch  } from 'react-redux';
import { useSelector } from 'react-redux';
import { useState } from "react"
import { useEffect } from "react"


function EditProduct(props) {
  const [articulo, setArtiiculo] = useState(props.articuloSeleccionado);
  const dispatch = useDispatch();
  const params = articulo;
  const articulosList = useSelector(state => state.articulos.value);

  const handleDelete = (idArticulo) => {
    dispatch(removeArticulo(articulo.idArticulo));
  };

  const handleChange = (e) => {
    setArtiiculo({
      ...articulo,
      [e.target.name]: e.target.value,
    });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    if (params.idArticulo) {
      dispatch(editArticulo(articulo));
    } else {
      dispatch(
        addArticulo({
          ...articulo,
        })
      );
    }
  };
  useEffect(() => {
    if (params.idArticulo) {
      setArtiiculo(articulosList.find((articulo) => articulo.idArticulo === params.idArticulo));
    }
  }, [params.idArticulo, articulosList]);

    return (
        <>
            <div className="contenedor-edit-product">
                <div className="contenedor-edit-product-tittle">
                    <h1 className='tittle-edit'>Editar Producto</h1>
                </div>
                <div className="contenedor-edit-product-form">
                    <form onSubmit={handleSubmit}>
                    <div className="contenedor-edit-product-form-edit-imagen">
                            <div className="contenedor-edit-product-form-edit-imagen-input">
                                <input type="file" name="imagen" id="imagen" />
                                <input type="submit" value="subir" className='btn'  />
                            </div>
                        </div>
                        <div className="contenedor-edit-product-form-edit-titulo">
                            <div className="contenedor-edit-product-form-edit-titulo-input">
                                <input type="text" name="nombre" placeholder="Titulo del producto" onChange={handleChange} value={articulo.nombre} />
                            </div>
                        </div>
                        <div className="contenedor-edit-product-form-edit-descripcion">
                            <div className="contenedor-edit-product-form-edit-descripcion-textarea">
                                <textarea name="descripcion" id="descripcion" cols="30" rows="10" placeholder="Descripcion del producto" onChange={handleChange} value={articulo.descripcion} ></textarea>
                            </div>
                        </div>
                        <div className="contenedor-edit-product-form-edit-color">
                            <div className="contenedor-edit-product-form-edit-color-input">
                                <input type="text" name="color" id="color" placeholder="color del producto" onChange={handleChange} />
                            </div>
                        </div>
                        <div className="contenedor-edit-product-form-edit-catetoria">
                            <div className="contenedor-edit-product-form-edit-catetoria-select">
                                <select name="categoria" id="categoria">
                                    <option value="Default" disabled>Seleccione un campo</option>
                                    <option value="Hombres">Hombres</option>
                                    <option value="mujeres">Mujeres</option>
                                    <option value="ninos">Niños</option>
                                    <option value="accesorios">Accesorios</option>
                                </select>
                            </div>
                        </div>
                        <div className="contenedor-edit-product-form-edit-precio">
                            <div className="contenedor-edit-product-form-edit-precio-input">
                                {/* poner un input numerico con limitacion de numeros negativos en el precio */}
                                <input type="number" name="precio" id="precio" placeholder="Precio del producto" min={10000} onChange={handleChange} value={articulo.precio} />
                            </div>
                        </div>
                        <div className="contenedor-edit-product-form-guardar">
                            <div className="contenedor-edit-product-form-botones-guardar-cancelar">
                                <button type="submit" className="btn-guardar" ><SaveAsIcon />Guardar</button>
                                <button type="button" className="btn-cancelar" onClick={() => handleDelete(articulo.id)} ><DeleteForeverIcon />Eliminar</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </>
    );
}

export default EditProduct;