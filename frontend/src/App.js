import Register from "./components/Register";
import RecoverPassword from "./components/RecoverPassword";
import Homepage from "./components/Homepage";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import UploadPost from "./components/UploadPost";
import Login from "./components/Login";


const App = () => {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          {/* <Route path="/register" element={<Register />} />
          <Route path="/password" element={<RecoverPassword />} />
          <Route path="/login" element={<Login />} /> */}
          <Route path="/homepage" element={<Homepage />} />
          <Route path="/create" element={<UploadPost />} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;