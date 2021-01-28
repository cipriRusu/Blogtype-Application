import React, { useEffect, useState } from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Card from 'react-bootstrap/Card'
import Media from 'react-bootstrap/Media'


const PostListingComponent = () => {
    const [values, updateData] = React.useState([])

    useEffect(() => {
        let mounted = true;
        fetch('http://localhost:4449/api/posts/')
            .then(response => response.json())
            .then(data => {
                if (mounted) {
                    updateData(data)
                }
            })
        return () => mounted = false;
    }, []
    )
    return (
        <Accordion>{values.map((value, index) =>
            <Card key={index}>
                <Accordion.Toggle as={Card.Header} eventKey={index + 1}>
                    <p>Post author: {value.author}</p>
                    <p>Post title: {value.title}</p>
                </Accordion.Toggle>
                <Accordion.Collapse eventKey={index + 1}>
                    <div style={{ margin: "20px" }}>
                        <Media>
                            <Media.Body>
                                <p>Post author: {value.author}</p>
                                <p>Post title: {value.title}</p>
                                <p>Post preview: {value.preview}</p>
                            </Media.Body>
                        </Media>
                    </div>
                </Accordion.Collapse>
            </Card>
        )}
        </Accordion>)
}

export default PostListingComponent