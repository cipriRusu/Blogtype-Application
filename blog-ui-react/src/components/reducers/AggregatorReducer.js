import AllDataReducer from './AllDataReducer';
import { combineReducers } from 'redux';

const AggregatorReducer = combineReducers({
    all_data: AllDataReducer
})

export default AggregatorReducer;