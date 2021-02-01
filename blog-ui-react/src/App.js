import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import PostListing from './components/PostListing'
import Post from './components/Post.js';
import Navigation from './components/Navigation'
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {
    return (
            <Router>
                <Navigation />
                <Switch>
                    <Route path="/posts" exact component={PostListing}></Route>
                    <Route path="/posts/:id" exact component={Post}></Route>
                </Switch>
            </Router>
    )
}

export default App