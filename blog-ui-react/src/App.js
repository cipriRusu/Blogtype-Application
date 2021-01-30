import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import Title from './components/Title'
import PostListing from './components/PostListing'
import Post from './components/Post.js';
import Navigation from './components/Navigation'

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {
    return (
        <div>
            <Router>
                <Navigation />
                <Title />
                <Switch>
                    <Route path="/post" component={Post}></Route>
                </Switch>
                <Switch>
                <Route path="/posts" component={PostListing}></Route>
                </Switch>
            </Router>
        </div>
    )
}

export default App