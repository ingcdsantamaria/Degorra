import React from 'react'
import MainNav from '../components/layout/MainNav'
import PiePagina from '../components/layout/Footer'
import '../components/stylesheets/Login.css'
import Botton from '../components/layout/Botton'

function Login() {
    return (
        <>
                <header className='main-header'>
                    <MainNav />
                </header>
                <main>
                    <div className="contenedor-login">
                        <div className="contenedor-login-tittle">
                            <h1 className="login-tittle">Iniciar sesión</h1>
                        </div>
                        <div className="contenedor-login-descripcion">
                            <p className="login-descripcion">Por favor, introduzca su correo y su contraseña:</p>
                        </div>
                        <div className="contenedor-login-form">
                            <form className="login-form">
                                <div className="contenedor-login-form-input">
                                    <input className="login-form-input" type="email" placeholder="Correo electrónico" />
                                </div>
                                <div className="contenedor-login-form-input">
                                    <input className="login-form-input" type="password" placeholder="Contraseña" />
                                    <a className="login-form-input-link" href="Recuperacion.jsx">¿Olvido su contraseña?</a>
                                </div>
                                <div className="contenedor-login-form-botton">
                                    <Botton
                                        texto="Iniciar sesión"
                                        href="./MainAdmin"
                                    />
                                </div>
                                <div className="contenedor-login-form-link">
                                    <p>¿No tienes una cuenta? <a href="./Register"> Crea una</a></p>
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

export default Login;