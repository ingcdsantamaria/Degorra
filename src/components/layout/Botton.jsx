import React from 'react'
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import '../stylesheets/Boton.css'


function Boton(props) {
    return (
        <>
            <div className="contenedor-login-form-button">
                <Stack spacing={2} direction="row">
                    <Button href={props.href} id="login-form-button" variant="contained">{props.texto}</Button>
                </Stack>
            </div>
        </>
    );
}

export default Boton;
