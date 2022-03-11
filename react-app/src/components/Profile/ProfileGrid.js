import React, { useState } from 'react'
import { useSelector } from 'react-redux';
import { Modal } from '../../context/Modal';
import { getProfilePostsArray } from '../../store/profile';
import PostView from '../PostView';
import ProfileGridItem from './ProfileGridItem';
// import PostEditForm from '../PostView/PostEditForm';

export default function ProfileGrid() {
  const [showIdx, setShowIdx] = useState(null);

  const posts = useSelector(getProfilePostsArray);

  const openPostView = (idx) => setShowIdx(idx);
  const closePostView = () => setShowIdx(null);
  return (
    <div className='profile-grid'>
      {posts.map((post, idx) => (
        // <div key={idx}>
        //   <img
        //     className='profile-grid-item'
        //     src={post.image_url}
        //     alt='user post'
        //     onClick={() => openPostView(idx)}
        //     style={{
        //       gridColumnStart: idx % 3 + 1
        //     }}
        //   />

        //   {showIdx === idx && (
        //     <Modal onClose={closePostView}>
        //       <PostView post={post} closePostView={closePostView} option='profile' />
        //     </Modal>
        //   )}
        // </div>
        <ProfileGridItem key={idx} post={post} idx={idx}/>

      ))}
    </div>
  )
}
