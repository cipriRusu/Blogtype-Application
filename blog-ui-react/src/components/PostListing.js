import React, { useEffect, useState } from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Card from 'react-bootstrap/Card'
import Media from 'react-bootstrap/Media'
import Button from 'react-bootstrap/Button'
import { useHistory } from "react-router-dom";
import usePostsData from './usePostsData'
import Post from './Post'

const PostListing = () => {
    const all_posts = usePostsData([]);
    return (all_posts.map(post => <Post post={post}/>))
}

export default PostListing