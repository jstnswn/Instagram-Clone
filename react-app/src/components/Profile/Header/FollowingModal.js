import React, { useState } from 'react'
import { useDispatch } from 'react-redux'
import { Link } from 'react-router-dom'

import { follow, unfollow } from '../../../store/dashboard'
import { Modal } from '../../../context/Modal';
import Unfollow from '../../UnfollowModal/Unfollow';
import x_btn from '../../../assets/x.png'
import './FollowerModal.css'

export default function FollowingFormModal({ profileUser, setNumberFollowing, userFollowing, setUserFollowing, user, closeModal}) {
    const dispatch = useDispatch()
    const [showUnfollowModal, setShowUnfollowModal] = useState(null)

    const handleFollow = (e, id) => {
        e.preventDefault()
        dispatch(follow(id))
        setUserFollowing(prev => [...userFollowing, id])
        if (profileUser.id === user.id) {
            setNumberFollowing(prev => ++prev)
        }
    }

    return (
        <>
            <div className='follower-heading'>
            <div className='x-btn-container'>
                <div className='follower-title'>Following</div>
                <img className='x-btn' src={x_btn} alt='Close Button'onClick={closeModal} />
            </div>
            </div>
            <div className='follower-modal-container'>

                {profileUser.following.map((followee, idx) => (
                    <div className='follower-info-container' key={`${followee.id}-followee`}>
                        <div className='follower-info'>
                            <img className='modal-img' src={followee.image_url} alt='Profile'></img>
                            <div className='follower-user-full'>
                                <Link onClick={closeModal} className='link' to={`/${followee.username}`}>
                                    {followee.username}
                                </Link>
                                <li className='modal-fullname'>{user.full_name}</li>
                            </div>
                        </div>
                        {(!userFollowing.includes(followee.id) && !(followee.id === user.id)) &&
                            <button className='modal-follow' onClick={(e) => handleFollow(e, followee.id)}>
                                Follow
                            </button>
                        }
                        {(userFollowing.includes(followee.id) && !(followee.id === user.id)) &&
                            <button className='modal-following' onClick={(e) => {
                                e.preventDefault()
                                setShowUnfollowModal(idx)
                            }}>
                                Following
                            </button>
                        }
                        {showUnfollowModal === idx &&
                            <Modal onClose={() => setShowUnfollowModal(false)} option='layer'>
                                <Unfollow
                                    user={followee}
                                    setShowUnfollowModal={setShowUnfollowModal}
                                    setUserFollowing={setUserFollowing}
                                    profileUser={profileUser}
                                    sessionUser={user}
                                    option='profile'
                                    setNumberFollowing={setNumberFollowing}
                                />
                            </Modal>
                        }
                    </div>
                ))}
            </div>
        </>
    )
}
