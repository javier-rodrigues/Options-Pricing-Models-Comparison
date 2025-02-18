import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Welcome from "./pages/Welcome";
import HowTo from "./pages/How_to"; // Updated path
import FAQ from "./pages/FAQ"; // Common Questions & Fixes page
import Tutorial from "./pages/Tutorial";
import IntermediateScreener from "./pages/Intermediate_Screener";
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
    <Router>
      <div>
        {/* Navigation Bar */}
        <nav style={navStyle}>
          <Link to="/" style={linkStyle}>Home</Link>
          <Link to="/welcome" style={linkStyle}>Welcome</Link>
          <Link to="/intermediate_screener" style={linkStyle}>Option Screener</Link>
        </nav>

        {/* Route Configuration */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/welcome" element={<Welcome />} />
          <Route path="/how_to" element={<HowTo />} /> {/* Updated path */}
          <Route path="/faq" element={<FAQ />} /> {/* This serves as the Common Questions page */}
          <Route path="/tutorial" element={<Tutorial />} />
          <Route path="/intermediate_screener" element={<IntermediateScreener />} />
        </Routes>
      </div>
    </Router>
  );
}

// Styling for the navigation bar
const navStyle = {
  display: "flex",
  justifyContent: "space-around",
  padding: "10px",
  backgroundColor: "#333",
  position: "sticky",
  top: 0,
  zIndex: 1000,
};

const linkStyle = {
  color: "white",
  textDecoration: "none",
  fontSize: "18px",
  padding: "8px 16px",
  borderRadius: "5px",
  backgroundColor: "#007bff",
};

export default App;
