import { normalizePosts } from "./utils";

const LOAD_POSTS = 'feed/LOAD_POSTS';

// Action Creators
const loadPosts = (data) => {
  return {
    type: LOAD_POSTS,
    data
  }
}

// Thunks
export const getFeedPosts = () => async dispatch => {
  const res = await fetch('/api/posts/');

  if (res.ok) {
    const data = await res.json();
    dispatch(loadPosts(data));
  } else {
    const errors = await res.json();
    console.log(errors);
  }
}


// Helper Functions
export const getFeedPostsArray = (state) => Object.values(state.feed.posts);


const initialState = {
  posts: null,
};

export default function reducer(state = initialState, action) {
  switch(action.type) {
    case LOAD_POSTS:
      const posts = normalizePosts(action.data.posts);
      return {
        ...state,
        posts: posts
      }
    default:
      return state
  }
};
