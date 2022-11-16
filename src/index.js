import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './redux/store';
// import { composeWithDevTools } from 'redux-devtools-extension';
// import MainWindow from './views/MainWindow'
// import { Routes, Route} from 'react-router-dom';
// import Login from './views/Login';
// import Register from './views/Register';
// import MainAdmin from './views/MainAdmin';
//import { AdminIzq } from './components/layout/AdminIzq';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Provider store={store}>
    <App />
    {/* <Routes>
      <Route path="/" element={<MainWindow />} />
      <Route path="login" element={<Login />} />
      <Route path="register" element={<Register />} />
      <Route path="mainadmin" element={<MainAdmin />} />
    </Routes> */}
    </Provider>
  </BrowserRouter>,
);

reportWebVitals();
