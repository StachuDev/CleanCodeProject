import Login from "./components/Login";
import Register from "./components/Register";
import RecoverPassword from "./components/RecoverPassword";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import UploadPost from "./components/UploadPost";

const App = () => {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/password" element={<RecoverPassword />} />
          <Route path="/login" element={<Login />} />
          <Route path="/create" element={<UploadPost />} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;