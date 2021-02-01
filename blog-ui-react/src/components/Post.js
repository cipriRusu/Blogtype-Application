import React from 'react'
import usePostsData from './usePostsData'

const Post = ({ match }) => {
	const post_data = usePostsData(`http://localhost:4449/api/posts/${match.params.id}`);
	return (
	<div style={{ display: 'grid', margin: '11px' }}>
		<h3>Post Title: {post_data.title}</h3>
		<h4>Post Author: {post_data.author}</h4>
		<hr/>
		<p>{post_data.content}</p>
	</div>)
}

export default Post