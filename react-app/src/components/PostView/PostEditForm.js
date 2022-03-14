import React, { useEffect, useRef, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { patchPost as updateDashboardPost, updatePost } from '../../store/dashboard';
import { patchPost as updateProfilePost } from '../../store/profile'

export default function PostEditForm({ post, closeEdit, closeMenu, option }) {
  const dispatch = useDispatch();
  const [caption, setCaption] = useState(post.caption);
  const [disableSubmit, setDisableSubmit] = useState(false);

  const feed = useSelector(({ dashboard }) => dashboard.feed);
  const feedPost = feed.postIds[post.id];

  const inputFocus = useRef(null);

  useEffect(() => {
    inputFocus.current.focus();
  }, [])

  useEffect(() => {
    if (caption.length > 2200) setDisableSubmit(true);
    else setDisableSubmit(false);
  }, [caption])


  const handleSubmit = async () => {
    if (disableSubmit) return;
    setDisableSubmit(true);

    const payload = { postId: post.id, caption };

    if (option === 'profile') {
      dispatch(updateProfilePost(payload));

      if (feedPost) dispatch(updatePost(post.id, caption))

    } else if (option === 'feed') {
      dispatch(updateDashboardPost(payload))
    }

    closeEdit()
    closeMenu()
  };

  return (

     <div id='post-form-container' className='final-form'>
      <div className='upload-post header'>
        <h3>Edit Post</h3>
        <p
          className={`next-button `}
          style={{
            opacity: caption.length > 2200 ? '50%' : '100%',
            cursor: caption.length > 2200 ? 'default' : 'pointer'
          }}
          onClick={handleSubmit}
        >Submit</p>
      </div>
      <div className='upload-form-container final'>
        <div className='image-container'>
          <img
            alt='post content'
            className='upload-image form'
            src={post.image_url}
          />
        </div>

        <div className='upload-form side-container'>
          <div className='post-form user-info'>
            <img
              alt='profile avatar'
              className='post-form profile-picture'
              src={post.user.image_url}
            />
            <p className='post-form username'>{post.user.username}</p>
          </div>
          <textarea
            className='comment-input'
            ref={inputFocus}
            value={caption}
            onChange={e => setCaption(e.target.value)}
            onFocus={e => e.currentTarget.setSelectionRange(e.currentTarget.value.length, e.currentTarget.value.length)}
          />
          <p
            className={`post-form word-count ${caption.length > 2200 ? 'active' : ''}`}
          >{`${caption.length}/2,200`}</p>
        </div>
      </div>
    </div>



  )
}
