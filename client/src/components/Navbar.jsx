import React from "react";
import "../styles/Navbar.css";
import { Link } from "react-router-dom";
const Navbar = () => {
  return (
    <div className="navbar">
      <div className="nav">
        <h1 className="name">DermAid ProVision</h1>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/Scans">Scans</Link>
          </li>
          <li>
            <Link to="/Derm">Derm</Link>
          </li>
          <li>
            <Link to="/About">About</Link>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
