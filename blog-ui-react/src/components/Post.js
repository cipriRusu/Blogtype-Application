import React from 'react'
import usePostsData from './usePostsData'

const Post = ({ match }) => {
	const post_data = usePostsData(`http://localhost:4449/api/posts/${match.params.id}`);
	return (
	<div style={{ margin: "20px", display: 'grid' }}>
		<h3>Post Title: {post_data.title}</h3>
		<h3>Post Author: {post_data.author}</h3>
		<p>{post_data.content}</p>
	</div>)
}

export default Post