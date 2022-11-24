import React from 'react'
import MainNav from '../components/layout/MainNav';
import PiePagina from '../components/layout/Footer';
import Botton from '../components/layout/Botton';
import '../components/stylesheets/Register.css';
import Input from '../components/layout/Input';


function Register() {
    return (
        <>
                <header className='main-header'>
                    <MainNav />
                </header>
                <main>
                    <div className="contenedor-registro">
                        <div className="contenedor-registro-tittle">
                            <h1 className="registro-tittle">Registro</h1>
                        </div>
                        <div className="contenedor-registro-descripcion">
                            <p className="registro-description">Por favor, complete la siguiente información:</p>
                        </div>
                        <div className="contenedor-registro-form">
                            <form className="registro-form">
                                    <Input
                                    type= 'text'
                                    placeholder= 'Username'
                                    />
                                    <Input
                                    type= 'text'
                                    placeholder= 'Nombre'
                                    />
                                    <Input
                                    type= 'text'
                                    placeholder= 'Apellidos'
                                    />
                                    <Input
                                    type= 'email'
                                    placeholder= 'Correo electronico'
                                    />
                                    <Input
                                    type= 'tel'
                                    placeholder= 'Telefono'
                                    />
                                    <Input
                                    type= 'password'
                                    placeholder= 'Contraseña'
                                    />
                                    <Input
                                    type= 'password'
                                    placeholder= 'Confirmar contraseña'
                                    />

                                <div className="contenedor-registro-form-input">
                                    <Botton
                                    texto= 'Registrarse'
                                    href= '../views/login'
                                    />
                                </div>
                                <div className="contenedor-registro-form-link">
                                    <p>¿Ya tienes una cuenta? <a href="./Login"> Inicia sesión</a></p>
                                </div>
                            </form>
                        </div>
                    </div>
                </main>
                <footer>
                    <PiePagina />
                </footer>

        </>
    );
}

export default Register;