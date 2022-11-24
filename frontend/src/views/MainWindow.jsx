import React from 'react'
import FeaturedProducts from '../components/layout/FeaturedProducts';
import MainNav from '../components/layout/MainNav';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Categorias from '../components/layout/Categories';
import PiePagina from '../components/layout/Footer';


// import { fetchAllArticulos } from '../redux/slices/articulos';
// import { useDispatch, useSelector } from 'react-redux';
//importamos los productos de la base de datos
// import {getProductsSuccess} from '../redux/Ducks/productoDuck';
// import {useDispatch, useSelector} from 'react-redux';

//exportamos la funcion Producto para poder usarla en otros archivos

function PrincipalWindow() {
    // const dispatch = useDispatch();
    // const [productTypeFromTab, setProductTypeFromTab] = React.useState(0);

    // React.useEffect(() => {
    //     dispatch(getProductsSuccess());
    // },[]);

    // const products = useSelector(store => store.products.product);

    // const info = {
    //     idArticulo: "619cc7d78011c2969719fedd",
    // }

    // const  kindOfArticulo=(value)=>{
    //     setProductTypeFromTab(value)
    //   }




    // const {list: articulos} = useSelector(state => state.articulos);
    // const dispatch = useDispatch();
    // useEffect(() => {
    //   dispatch(fetchAllArticulos());
    // }, [dispatch]);
    
    return (
        <>
                <header className='main-header'>
                    <h1 id='header'>Un nuevo concepto de moda</h1>
                    <MainNav />
                </header>
                <main>
                    {/* <div className='main-content'>
                        <div className='row'>
                            {
                                articulos.map((articulos, index) => (
                                    <div key={index} className='col-md-3'>
                                        <div className='card'>
                                            <h3>{articulos.nombre}</h3>
                                            <p>{articulos.descripcion}</p>
                                            <p>{articulos.precio}</p>
                                            <p>{articulos.color}</p>
                                        </div>
                                    </div>
                                ))
                            }
                        </div>
                    </div> */}
                    {/* <div>
                        {
                        productTypeFromTab===0?
                        products==="error"?'mostrar error con el cosito ed abajo con el tipo de error':
                        products.map(item=>(
                            <div key={item._id}>
                                <p>{item.name}</p>
                                <p>{item.description}</p>
                                <p>{item.price}</p>
                                <p>{item.color}</p>
                            </div>
                        )):null}
                    </div> */}
                    <div className="contenedor-portada">
                        <div className="contenedor-portada-tittle">
                            <h1 className="portada-tittle">Tienda de gorras</h1>
                        </div>
                    </div>
                    <div className="contenedor-productos-destacados">
                        <h2 className="productos-destacados-tittle">Productos destacados</h2>
                        <div className="contenedor-productos">
                            <FeaturedProducts
                            imagen= 'motociclista'
                            titulo= 'GORRA DE motociclista'
                            precio= '50.000'
                            />
                            <FeaturedProducts
                            imagen= 'pixelada'
                            titulo= 'GORRA pixelada'
                            precio= '100.000'
                            />
                        </div>
                    </div>
                    <div className="boton-ver-mas">
                        <Stack spacing={2} direction="row">
                            <Button id="boton" variant="contained">Ver mas...</Button>
                        </Stack>
                    </div>
                    <div className="contenedor-categorias-productos">
                        <Categorias
                        imagen= 'mujeres'
                        formato= 'jpg'
                        categoria= 'Mujeres'
                        />
                        <Categorias
                        imagen= 'hombres'
                        formato= 'jpg'
                        categoria= 'Hombres'
                        />
                        <Categorias
                        imagen= 'accesorios'
                        formato= 'jpeg'
                        categoria= 'Accesorios'
                        />
                    </div>
                </main>
                <footer>
                    <PiePagina />
                </footer>

        </>
    );
}

export default PrincipalWindow;