import React from 'react'
import usePostsData from './usePostsData'
import './PostStyle.sass'

const Post = ({ match }) => {
	const post_data = usePostsData(`http://localhost:4449/api/posts/${match.params.id}`);
	return (
	<div className="PostContainer">
		<div className="PostHeaderContainer">
			<h3>Post Title: {post_data.title}</h3>
			<h4>Post Author: {post_data.author}</h4>
		</div>
		<div className="PostContentContainer">
			<p>{post_data.content}</p>
		</div>
	</div>)
}

export default Post