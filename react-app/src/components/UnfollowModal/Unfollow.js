import React from "react";
import { useDispatch } from "react-redux";
import { unfollow } from "../../store/dashboard";
import './Unfollow.css'


export default function Unfollow({ user, setShowUnfollowModal, option, setUserFollowing, setNumberFollowers, sessionUser, profileUser, setNumberFollowing }) {
    const dispatch = useDispatch();

    const handleUnfollow = (e) => {
        e.preventDefault()
        dispatch(unfollow(user.id))
        setShowUnfollowModal(false)
        // && setUserFollowing is temporary
        if (option === 'profile-direct' && setUserFollowing) {
            setUserFollowing(prev => prev.filter(followId => followId !== user.id))
            setNumberFollowers(prev => --prev)
        }
        if (option === 'profile') {
            setUserFollowing(prev => prev.filter(followId => followId !== user.id))
            if (sessionUser.id === profileUser.id) {
                setNumberFollowing(prev => --prev)
            }
        }
    }

    return (
        <div id='unfollow-modal-container'>
            <img src={user.image_url} className='feed-profile-pic' id='unfollow-profile-pic' alt='profile-pic'></img>
            <div className="unfollow-modal-username">Unfollow @{user.username}?</div>
            <div className="unfollow-mobal-btn-container">
                <div className='modal-unfollow-btn red' onClick={handleUnfollow}>Unfollow</div>
                <div className='modal-cancel-btn' onClick={(e) => setShowUnfollowModal(false)}>Cancel</div>
            </div>
        </div>
    )
}
