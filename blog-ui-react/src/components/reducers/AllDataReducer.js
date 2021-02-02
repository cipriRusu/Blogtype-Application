const AllDataReducer = (state = [], action) => {
    switch(action.type){
        case 'GET_ALL_DATA':
            fetch(action.payload)
            .then(response => response.json())
            .then(data => data.map(x => state.push(x)))
            return state
        default:
            return state;
    }
}

export default AllDataReducer