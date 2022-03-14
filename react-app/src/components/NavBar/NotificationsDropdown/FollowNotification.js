import React from 'react'
import { Link } from 'react-router-dom'

export default function FollowNotification({ follows }) {

  return (
    <>
      <p>Follows</p>
      {follows.map((follow, idx) => (
        <div className='notification-container dd' key={idx}>
          <div className='notification follow user-info dd'>
            <img alt='user avatar' className='dd' src={follow.from_user.image_url} />
            <Link to={`/${follow.from_user.username}`} className='notification-username'>{follow.from_user.username}</Link>
            <p className='dd'>started following you</p>
          </div>
          {/* <img className='post-notification-image' alt='post' src={follow.post.image_url} /> */}
          {/* <button onClick={(e) => toggleFollow(e, follow.from_user.id)}className={!followed ? 'modal-follow dd' : 'modal-following'}>Follow</button>x */}
        </div>
      ))}
    </>
  )
}
