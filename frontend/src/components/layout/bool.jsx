// import React from 'react'
import { useState} from 'react'

function Changebool() {
        let [bool, setBool] = useState(false);
        console.log(bool);
        const Change=()=>{
            setBool(!bool);
            console.log(bool);
            return bool;
        }
        return Change;
}


export default Changebool;