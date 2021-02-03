import React from 'react';
import Accordion from 'react-bootstrap/Accordion';
import PostListed from './PostListed';
import { useSelector, useDispatch } from 'react-redux';
import { GetDataAction } from './actions/GetDataAction';

const PostListing = () => {
    const all_data = useSelector(state => state.all_data)

    const dispatch = useDispatch();
    
    React.useEffect(() => dispatch(GetDataAction('http://localhost:4449/api/posts/')),[]);

    return (
    <Accordion>
        {all_data.posts.map((post, index) => (<PostListed post={post} count={index}/>))}
    </Accordion>)
}

export default PostListing