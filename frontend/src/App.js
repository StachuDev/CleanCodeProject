import Register from "./components/Register";
import RecoverPassword from "./components/RecoverPassword";
import Homepage from "./components/Homepage";
import PostPage from "./components/PostPage";
import { BrowserRouter as Router, Route, Routes} from "react-router-dom";

const App = () => {
  return (
    <div className="App">
    <Router>
      <Routes>
        <Route path="/" element={<Homepage />} />
        {/* <Route path="/register" element={<Register />} />
        <Route path="/password" element={<RecoverPassword />} />
        <Route path="/login" element={<Login />} /> */}
        <Route path="/homepage" element={<Homepage/>}/>
        <Route path="/post" element={<PostPage/>}/>
      </Routes>
  </Router>
  </div>
  );
};

export default App;