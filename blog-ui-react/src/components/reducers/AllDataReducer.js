import React, { setState } from 'react';

const AllDataReducer = (state = [], action) => {
    switch(action.type){
        case 'GET_ALL_DATA':
            return state
        default:
            return state;
    }
}

export default AllDataReducer