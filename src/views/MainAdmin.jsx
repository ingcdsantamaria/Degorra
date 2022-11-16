import React from 'react'
import NavAdmin from '../components/layout/Nav';
import '../components/stylesheets/MainAdmin.css';
import PiePagina from '../components/layout/Footer';
import AdminDerec from '../components/layout/AdminDerec';
// import AdminIzq from '../components/layout/AdminIzq';
import {AdminIzq} from '../components/layout/AdminIzq';
import SplitPane from 'react-split-pane';
import { useState} from 'react'



function MainAdmin() {

    const [bool, setBool] = useState(false);
    const handleChangeBool = () => {
        setBool((prevBool) => !prevBool);
    };

    return (
        <>
                <header className='main-header'>
                    <NavAdmin />
                </header>
                <main>
                <div className="contenedor-main-admin">
                    <SplitPane className="splitpane" split="vertical" defaultSize={520} primary="second">
                        <AdminIzq onChange={handleChangeBool} />
                        <AdminDerec change={bool} />
                    </SplitPane>
                </div>
                </main>
                <footer>
                    <PiePagina />
                </footer>
        </>
    );
}

export default MainAdmin;