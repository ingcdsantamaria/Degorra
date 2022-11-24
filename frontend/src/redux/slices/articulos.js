
import { createSlice } from '@reduxjs/toolkit'
import api from '../../api/backend'


export const articuloSlice = createSlice({
  name: 'articulos',
  initialState: {
    value: [],
  },
  reducers: {
        addArticulo: (state, action) => {
          state.value.push(action.payload)
        },
        setArticulosList: (state, action) => {
          state.value = action.payload;
        },
          updateArticulo: (state, action) => {
            console.log(action.payload);
            const { idArticulo, nombre, descripcion, precio, color } = action.payload;
            console.log(state);
            const existingArticulo = state.value.find(articulo => articulo.idArticulo === idArticulo);
            console.log(existingArticulo);
            if(existingArticulo) {
              existingArticulo.idArticulo = idArticulo;
              existingArticulo.nombre = nombre;
              existingArticulo.descripcion = descripcion;
              existingArticulo.precio = precio;
              existingArticulo.color = color;
            }
          },
        deleteArticulo: (state, {payload: index}) => {
          state.value.splice(index, 1);
        },
      }
    },
)

export const { setArticulosList, addArticulo, updateArticulo, deleteArticulo } = articuloSlice.actions;

export default articuloSlice.reducer;

export const fetchAllArticulos = () => (dispatch) => {
    api.get('/articulo/').then(res => {
      dispatch(setArticulosList(res.data));
    })
    .catch((error) => console.log(error));
}

//agregar articulo
export const createArticulo = (articulo) => (dispatch) => {
    api.post('/articulo/', articulo)
    .then(res => {
        dispatch(addArticulo(res.data));
    })
    .catch((error) => console.log(error));
}
//actualizar articulo
export const editArticulo = (articulo) => (dispatch) => {
  api.put(`/articulo/${articulo.idArticulo}/`,articulo)
  .then(res => {
      dispatch(updateArticulo(res.data));
  })
  .catch((error) => console.log(error));
}
//eliminar articulo
export const removeArticulo = (idArticulo) => (dispatch) => {
    api.delete(`/articulo/${idArticulo}/`, idArticulo)
    .then(res => {
        dispatch(deleteArticulo(res.data));
    })
    .catch((error) => console.log(error));
}
