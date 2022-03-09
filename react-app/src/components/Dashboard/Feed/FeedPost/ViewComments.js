
import './ViewComments.css'
import {useSelector} from 'react-redux';
import PostView from '../../../PostView';



function ViewComments ({post}) {

    const id = post.id
    // console.log(id, "this is post id")
    const comments = useSelector(state=>state.dashboard.feed.postIds[id].comments)
    const commentsArray = Object.values(comments)
    // console.log(commentsArray, 'this is commentsarray')

    // if (commentsArray.length > 0){
    //     const firstLast = commentsArray.length-1;
    //     const secondLast = commentsArray.length-2;

    //     const firstLastComment = commentsArray[firstLast].comment
    //     const secondLastComment = commentsArray[secondLast].comment

    // }
    // const firstLast = commentsArray.length-1;
    // const secondLast = commentsArray.length-2;



    return  (
        <div className="view-comments-container">
            {/* {commentsArray.length > 0 ? <PostView/> : null} */}
            {commentsArray.length > 0 ? <div className="expand-view-comments">View all {commentsArray.length} comments</div> : null}
            {/* {commentsArray.length>0 ? <ol><li>{commentsArray[commentsArray.length-1].comment}</li><li>{commentsArray[commentsArray.length-2].comment}</li></ol>: null} */}
            {commentsArray.length>0 ? <div>{commentsArray[commentsArray.length-1].username} {commentsArray[commentsArray.length-1].comment}</div>: null}
            {commentsArray.length>1 ? <div>{commentsArray[commentsArray.length-2].comment}</div>: null}


        </div>
    )

}


export default ViewComments;
