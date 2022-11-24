import React from 'react'

function Input(props) {
    return (
        <>
            <div className="contenedor-registro-form-input">
                <input className="registro-form-input" type={props.type} placeholder={props.placeholder} />
            </div>
        </>
    );
}

export default Input;