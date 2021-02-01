import React from 'react'
import Accordion from 'react-bootstrap/Accordion'
import usePostsData from './usePostsData'
import PostListed from './PostListed'

const PostListing = () => {
    const post_data = usePostsData('http://localhost:4449/api/posts/');
    return (
    <Accordion>
        {post_data.map((post, index) => (<PostListed post={post} count={index}/>))}
    </Accordion>
    )
}

export default PostListing