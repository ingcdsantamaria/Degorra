import { configureStore } from '@reduxjs/toolkit'
// import articulos from './slices/articulos'
import articulosReducer from './slices/articulos'

export default configureStore({
    reducer: {
        articulos: articulosReducer,
    }
})