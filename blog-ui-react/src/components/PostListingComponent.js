import React from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Card from 'react-bootstrap/Card'

const PostListingComponent = () => {
    const [values, updateData] = React.useState([])

    fetch('http://localhost:4449/api/posts/')
        .then(response => response.json())
        .then(data => updateData(data))
    return (
        <Accordion>{values.map((value, index) =>
            <Card key={index}>
                <Accordion.Toggle as={Card.Header} eventKey={index + 1}>
                    <p>Post author: {value.author}</p>
                    <p>Post title: {value.title}</p>
                </Accordion.Toggle>
                <Accordion.Collapse eventKey={index + 1}>
                    <Card.Body>
                        <p>Post author: {value.author}</p>
                        <p>Post title: {value.title}</p>
                        <p>Post preview: {value.preview}</p>
                    </Card.Body>
                </Accordion.Collapse>
            </Card>
        )}
        </Accordion>)
}

export default PostListingComponent