const initialState = { post: {} }

const PostDataReducer = (state = initialState, action) => {
    switch(action.type){
        case 'GET_POST_DATA':
            let post_data = {}
            fetch(action.payload)
            .then(response => response.json())
            .then(data => Object.assign(post_data, data))
            return {...state, post: post_data}
        default:
            return state;
    }
}

export default PostDataReducer