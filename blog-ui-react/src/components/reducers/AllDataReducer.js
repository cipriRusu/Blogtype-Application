const initialState = { posts: [] }

const AllDataReducer = (state = initialState, action) => {
    switch(action.type){
        case 'GET_ALL_DATA':
            let all_posts = []
            fetch(action.payload)
            .then(response => response.json())
            .then(data => data.map(x => all_posts.push(x)))
            return {...state, posts: all_posts}
        default:
            return state;
    }
}

export default AllDataReducer