import api from '../api/backend';

// creamos una funcion success que recibe como parametro (Data, completed) y retorna un objeto con la propiedad type y la propiedad payload
function Success(Data, Completed) {
    return {
        data: Data,
        completed: Completed,
        }
    };
// creamos una funcion error que recibe como parametro (error, completed) y retorna un objeto con la propiedad type y la propiedad payload
function Error(Error, Completed) {
    return {
        error: Error,
        completed: Completed,
        }
    }

//mostar todos los productos
export async function ShowProducts(info) {
    try{
    const ShowProduct = await api.get('/articulo' + info.idArticulo);
    return new Success(ShowProduct, true)
    }catch(error){
        return new Error(`${error}`, false);
    }
}