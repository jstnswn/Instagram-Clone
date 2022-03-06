import React, { useEffect, useState } from 'react'
import { useDispatch } from 'react-redux'
import { getFeedPosts } from '../../store/feed'
import './Dashboard.css'
import Feed from './Feed'

export default function Dashboard() {
  const dispatch = useDispatch()
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(getFeedPosts())
      .then(() => setIsLoaded(true))
  }, [dispatch])

  return isLoaded && (
    <div id='dashboard-container'>
      <div>Petstagram</div>
      <div className='feed-container'>
        <Feed />
      </div>
    </div>
  )
}