const defaultState = {
    git: [],
    job: {}
}

const jobReducer = (state = defaultState, action) => {
    switch(action.type){
        case "FETCH_JOBS":
            return {
                ...state,
                jobs: [...action.payload],
            }
        case "FETCH_JOB":
            return {
                ...state,
                job: {...action.payload} 
            }
    
        default: return state
    }
}

export default jobReducer;