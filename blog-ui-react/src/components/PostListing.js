import React, { Fragment } from 'react'
import Accordion from 'react-bootstrap/Accordion'
import usePostsData from './usePostsData'
import PostListed from './PostListed'

const PostListing = () => {
    const all_posts = usePostsData([]);
    return (
    <Accordion>
        {all_posts.map((post, index) => (<PostListed post={post} count={index}/>))}
    </Accordion>
    )
}

export default PostListing