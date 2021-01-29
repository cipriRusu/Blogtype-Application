import React, { useEffect, useState } from 'react'
import NavComponent from './NavComponent'
import {
	useRouteMatch 
} from "react-router-dom";


const PostComponent = () => {
    let match = useRouteMatch("/post/:id");
    const [value, updateData] = React.useState({});

    useEffect(() => {
        let mounted = true;
        fetch('http://localhost:4449/api/posts/'.concat(match.params.id))
            .then(response => response.json())
            .then(data => {
                if (mounted) {
                    updateData(data)
                }
            })
        return () => mounted = false;
    }, []
    )

	return (<div>
        <NavComponent />
        <p> {value.author   } </p>
		</div>)
}

export default PostComponent