import React from 'react'
import NavAdmin from '../components/layout/Nav';
import '../components/stylesheets/MainAdmin.css';
import PiePagina from '../components/layout/Footer';
import AdminDerec from '../components/layout/AdminDerec';
// import AdminIzq from '../components/layout/AdminIzq';
import AdminIzq from '../components/layout/AdminIzq';
import SplitPane from 'react-split-pane';
import { useState} from 'react'
import { useSelector } from 'react-redux';

// import { fetchAllArticulos } from '../redux/slices/articulos';
// import { useDispatch, useSelector } from 'react-redux';


function MainAdmin() {
    const articulosList = useSelector(state => state.articulos.value);
    const [articuloSeleccionado, setArticuloSeleccionado] = useState({});


    const [bool, setBool] = useState(false);
    const handleChangeBool = () => {
        setBool((prevBool) => !prevBool);
    };

    const [change, setChange] = useState(false);
    const handleChange = () => {
        setChange((prevChange) => !prevChange);
    };

    return (
        <>
                <header className='main-header' >
                    <NavAdmin />
                </header>
                <main>
                <div className="contenedor-main-admin">
                    <SplitPane className="splitpane" split="vertical" defaultSize={520} primary="second">
                        <AdminIzq onChange={handleChangeBool} inchange={handleChange} articulosList={articulosList} setArticulo={setArticuloSeleccionado} />
                        <AdminDerec change={bool} new={change} articulo={articuloSeleccionado} />
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