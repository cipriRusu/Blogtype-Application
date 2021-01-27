import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import TitleComponent from './components/TitleComponent'
import PostListingComponent from './components/PostListingComponent'
import NavComponent from './components/NavComponent'
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

function App() {
    return (
        <div>
            <TitleComponent />
            <Router>
                <NavComponent />
                <Switch>
                    <Route path="/posts" component={PostListingComponent}></Route>
                </Switch>
            </Router>
        </div>
    )
}

export default App