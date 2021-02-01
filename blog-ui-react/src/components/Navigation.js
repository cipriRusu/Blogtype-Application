import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import './NavigationStyling.css'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav';
import { NavLink } from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

const Navigation = () => {
    return (
        <Navbar style={{ padding: "0px", paddingTop: "20px", paddingBottom: "20px"}} bg="dark" variant="dark" fixed="static-top">
            <Nav.Link style={{ padding: "0px", paddingRight: "50px", paddingLeft:"11px"}}><Link to='/posts'>Posts</Link></Nav.Link>
            <Nav.Link style={{ padding: "0px", paddingRight: "50px"}}><Link to='/users'> Users</Link></Nav.Link>
            <Nav.Link style={{ padding: "0px", paddingRight: "50px"}}><Link to='/stats'> Statstics</Link></Nav.Link>
        </Navbar>
    )
}

export default Navigation