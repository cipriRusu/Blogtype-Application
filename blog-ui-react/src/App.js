import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import TitleComponent from './components/TitleComponent'
import PostListingComponent from './components/PostListingComponent'
import NavComponent from './components/NavComponent'

function App() {
    return (
        <div>
            <NavComponent />
            <TitleComponent />
            <PostListingComponent />
        </div>
    )
}

export default App