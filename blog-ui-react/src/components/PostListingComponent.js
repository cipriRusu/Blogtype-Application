import React, { useState } from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Card from 'react-bootstrap/Card'

const PostListingComponent = () => {
    const [values, updateData] = React.useState([])

    fetch('http://localhost:4449/api/posts/')
        .then(response => response.json())
        .then(data => updateData(data))
    return (
        <Accordion>{values.map((value, index) =>
            <Card>
                <Accordion.Toggle as={Card.Header} eventKey={index + 1}>
                    <p>{value.author}</p>
                    <p>{value.title}</p>
                </Accordion.Toggle>
                <Accordion.Collapse eventKey={index + 1}>
                    <Card.Body>
                        <p>{value.author}</p>
                        <p>{value.title}</p>
                        <p>{value.preview}</p>
                    </Card.Body>
                </Accordion.Collapse>
            </Card>
        )}
        </Accordion>)
}

export default PostListingComponent