import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav';
import { NavLink } from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

const NavComponent = () => {
    return (
        <Navbar fixed="top">
            <Nav.Link><Link to='/posts'>Posts</Link></Nav.Link>
            <Nav.Link><Link> Users</Link></Nav.Link>
            <Nav.Link><Link> Statstics</Link></Nav.Link>
        </Navbar>
    )
}

export default NavComponent