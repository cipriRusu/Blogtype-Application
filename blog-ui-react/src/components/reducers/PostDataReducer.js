const PostDataReducer = (state = {}, action) => {
    switch(action.type){
        case 'GET_POST_DATA':
            fetch(action.payload)
            .then(response => response.json())
            .then(data => Object.assign(state, data))
            console.log(state)
            return state
        default:
            return state;
    }
}

export default PostDataReducer