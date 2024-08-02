import React from 'react';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import './App.css'
import Home from "./components/Home";
import Derm from "./components/Derm";
import Scans from "./components/Scans";
import About from "./components/About";
import Navbar from './components/Navbar';
const App = () => {
  return (
    <div>
      <Navbar/>
        <Routes>
          <Route path = '/' element = {<Home />}/>
          <Route path = '/Derm' element = {<Derm />}/>
          <Route path = '/Scans' element = {<Scans />}/>
          <Route path = '/About' element = {<About />}/>
        </Routes>
    </div>
  );
};

export default App;