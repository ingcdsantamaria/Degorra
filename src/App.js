
import './App.css';
import MainWindow from './views/MainWindow'
import { Routes, Route} from 'react-router-dom';
import Login from './views/Login';
import Register from './views/Register';
import MainAdmin from './views/MainAdmin';


function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<MainWindow />} />
          <Route path="login" element={<Login />} />
          <Route path="register" element={<Register />} />
          <Route path="mainadmin" element={<MainAdmin />} />
      </Routes>
        {/* <Route path="/" element={<MainWindow />} />
      </Routes>
      <Routes>
        <Route path="/login" element={<Login />} />
      </Routes>
      <Routes>
        <Route path="/register" element={<Register />} />
      </Routes>
      <Routes>
        <Route path="/mainadmin" element={<MainAdmin />} />
      </Routes> */}
    </div>
  );
}

export default App;
