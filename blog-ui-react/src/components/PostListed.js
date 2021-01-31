import React from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Card from 'react-bootstrap/Card'
import Media from 'react-bootstrap/Media'
import Button from 'react-bootstrap/Button'

const PostListed = (props) => {
    return (
    <Card>
        <Accordion.Toggle as={Card.Header} eventKey={props.count + 1}>
            <p>Post author: {props.post.author}</p>
            <p>Post title: {props.post.title}</p>
            </Accordion.Toggle>
            <Accordion.Collapse eventKey={props.count + 1}>
                <div style={{ margin: "20px" }}>
                    <Media>
                        <Media.Body>
                            <p>Post author: {props.post.author}</p>
                            <p>Post title: {props.post.title}</p>
                            <p>Post preview: {props.post.preview}</p>
                        </Media.Body>
                        <img
                        width={160}
                        height={100}
                        className="mr-3"
                        src={props.post.image_path}
                        alt="Generic placeholder"
                        />
                    </Media>
                    <Button type="button" outline variant="secondary" size="sm">Go To Post</Button>
                </div>
            </Accordion.Collapse>
    </Card>)
}

export default PostListed