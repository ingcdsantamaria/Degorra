import React from 'react'
import '../stylesheets/Footer.css'

function Footer() {
    return (
        <>
            <div className="contenedor-footer">
                <ul className="tabla-footer">
                    <li className="tabla-footer-item">
                        <a href="FAQs.jsx">FAQs</a>
                    </li>
                    <li className="tabla-footer-item">
                        <a href="Contacto.jsx">Contacto</a>
                    </li>
                    <li className="tabla-footer-item">
                        <a href="PrivacyPolicies.jsx">Politicas de privacidad</a>
                    </li>
                    <li className="tabla-footer-item">
                        <a href="Terms.jsx">Terminos y condiciones</a>
                    </li>
                </ul>
                <div className="contenedor-footer-copyright">
                    <p className="copyright">&#169; TIENDA DEGORRA</p>
                </div>
            </div>
        </>
    );
}

export default Footer;