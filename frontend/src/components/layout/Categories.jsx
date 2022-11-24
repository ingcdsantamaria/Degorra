import React from 'react'
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import '../stylesheets/WomanProducts.css';

function Categories(props) {
    return (
        <>
            <div className="contenedor-categorias">
                <div className="contenedor-categorias-img">
                    <img className='categorias-img' src={require(`../images/imagen-categorias-${props.imagen}.${props.formato}`)} alt="categorias de productos"/>
                </div>
                <div className="contenedor-categorias-tittle">
                    <h3 className="categorias-tittle">{props.categoria}</h3>
                </div>
                <div className="contenedor-categorias-boton">
                    <Stack spacing={2} direction="row">
                        <Button id="categorias-boton" variant="outlined">Ver productos</Button>
                    </Stack>
                </div>
            </div>
        </>
    );
}

export default Categories;