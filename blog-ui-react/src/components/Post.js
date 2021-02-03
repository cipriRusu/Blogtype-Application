import React from 'react'
import { useSelector, useDispatch } from 'react-redux';
import './PostStyle.sass'
import { GetPostDataAction } from './actions/GetPostDataAction';

const Post = ({ match }) => {
	const post_data = useSelector(state => state.post_data)

	const dispatch = useDispatch();

	React.useEffect(() => dispatch(GetPostDataAction(`http://localhost:4449/api/posts/${match.params.id}`)),[]);

	return (
	<div className="PostContainer">
		<div className="PostHeaderContainer">
			<h3>Post Title: {post_data.title}</h3>
			<h4>Post Author: {post_data.author}</h4>
		</div>
		<div className="PostContentContainer">
			<p>{post_data.post.content}</p>
		</div>
	</div>)
}

export default Post