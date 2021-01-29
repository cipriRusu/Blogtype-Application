import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import TitleComponent from './components/TitleComponent'
import PostListingComponent from './components/PostListingComponent'
import PostComponent from './components/PostComponent.js';
import NavComponent from './components/NavComponent'
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {
    return (
        <div>
            <Router>
                <NavComponent />
                <TitleComponent />
                <Switch>
                    <Route path="/post" component={PostComponent}></Route>
                </Switch>
                <Switch>
                    <Route path="/posts" component={PostListingComponent}></Route>
                </Switch>
            </Router>
        </div>
    )
}

export default App