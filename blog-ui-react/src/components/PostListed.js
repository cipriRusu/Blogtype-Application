import React, { useState } from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Card from 'react-bootstrap/Card'
import Media from 'react-bootstrap/Media'
import Button from 'react-bootstrap/Button'
import { Link } from 'react-router-dom';

const PostListed = (props) => {
    return (
    <Card>
        <Accordion.Toggle as={Card.Header} eventKey={props.count + 1} style={{ padding: "0px", paddingLeft: "10px", paddingTop: "20px", paddingBottom: "20px"}}>
            <p style={{ margin: "0px"}}>Post author: {props.post.author}</p>
            <p style={{ margin: "0px"}}>Post title: {props.post.title}</p>
            </Accordion.Toggle>
            <Accordion.Collapse eventKey={props.count + 1} style={{ paddingLeft: "10px"}}>
                <div style={{ paddingTop: "20px", paddingBottom: "20px"}}>
                    <Media>
                        <Media.Body>
                            <p style={{ margin: "0px"}}>Post author: {props.post.author}</p>
                            <p style={{ margin: "0px"}}>Post title: {props.post.title}</p>
                            <p style={{ margin: "0px"}}>Post preview: {props.post.preview}</p>
                        </Media.Body>
                        <img
                        style={{ marginRight: "20px"}}
                        width={160}
                        height={100}
                        src={props.post.image_path}
                        alt="Generic placeholder"
                        />
                    </Media>
                    <Link to={`/posts/${props.post.post_id}`}>
                        <Button type="button" outline variant="secondary" size="sm">Go To Post</Button>
                    </Link>
                </div>
            </Accordion.Collapse>
    </Card>)
}

export default PostListed