import Login from "./components/Login";
import Register from "./components/Register";
import RecoverPassword from "./components/RecoverPassword";
import { BrowserRouter as Router, Route, Routes} from "react-router-dom";

const App = () => {
  return (
    <div className="App">
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/password" element={<RecoverPassword />} />
        <Route path="/login" element={<Login />} />
      </Routes>
  </Router>
  </div>
  );
};

export default App;