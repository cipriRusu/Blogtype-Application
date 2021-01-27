import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import PostComponent from './PostComponent.js';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav';
import { NavLink } from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

const NavComponent = () => {
    return (
        <Navbar>
            <Nav><Link to='/posts'>Posts</Link></Nav>
            <Link>Users</Link>
            <Link>Statstics</Link>
        </Navbar>
    )
}

export default NavComponent