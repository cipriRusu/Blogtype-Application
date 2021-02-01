import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav';
import { NavLink } from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

const Navigation = () => {
    return (
        <Navbar bg="dark" variant="dark" fixed="static-top">
            <Nav.Link><Link to='/posts'>Posts</Link></Nav.Link>
            <Nav.Link><Link to='/users'> Users</Link></Nav.Link>
            <Nav.Link><Link to='/stats'> Statstics</Link></Nav.Link>
        </Navbar>
    )
}

export default Navigation