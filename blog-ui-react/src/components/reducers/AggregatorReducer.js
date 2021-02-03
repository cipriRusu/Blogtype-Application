import AllDataReducer from './AllDataReducer';
import PostDataReducer from './PostDataReducer';
import { combineReducers } from 'redux';

const AggregatorReducer = combineReducers({
    all_data: AllDataReducer,
    post_data: PostDataReducer
})

export default AggregatorReducer;