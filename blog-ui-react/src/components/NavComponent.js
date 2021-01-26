import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from 'react-bootstrap/Navbar'
import { NavLink } from 'react-bootstrap';

const NavComponent = () => {
    return (
        <Navbar bg="dark" variant="dark" sticky="top">
            <NavLink href="#test">Posts</NavLink>
            <NavLink href="#test">Users</NavLink>
            <NavLink href="#test">Add Post</NavLink>
    </Navbar>)
}

export default NavComponent