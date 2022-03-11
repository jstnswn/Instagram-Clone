import { useDispatch, useSelector } from "react-redux"
import { useState } from "react";
import "./CommentForm.css"
import { createCommentDashboard } from "../../store/dashboard";
import { createCommentProfile } from "../../store/profile";
import { addComment } from "../../store/dashboard";

function CommentForm({ option, post}) {
    const dispatch = useDispatch();

    console.log(option, 'this is option')
    const currentUser = useSelector(state => state.session.user);

    const [comment, setComment] = useState("");
    const [errors, setErrors] = useState([]);


    const handleSubmitDashboard = async (e) => {
        e.preventDefault();
        const postId = post.id


        const payload = {

            user_id: currentUser.id,
            post_id: postId,
            comment,
        }


        let newComment = await dispatch(createCommentDashboard(payload))
        // .catch(async(res)=>{
        //     const data = await res.json();
        //     if(data && data.errors) return setErrors(data.errors)
        // })
    }

    const handleSubmitProfile = async (e) => {
        e.preventDefault();
        const postId = post.id
        console.log("in here")

        const payload = {

            user_id: currentUser.id,
            post_id: postId,
            comment,
        }

        let newComment = await dispatch(createCommentProfile(payload))
        console.log(newComment, 'this is newComment')
        if(newComment){


            dispatch(addComment(newComment))
        }


    }



    if (option === 'feed') {

        return (

            <div>

                <form onSubmit={handleSubmitDashboard}>
                    <div className="comment-form-container">
                        <textarea
                            id={post.id}
                            className="comment-form-textarea"
                            cols="74"
                            placeholder="Add a comment..."
                            value={comment}
                            onChange={(e) => setComment(e.target.value)}
                        >
                        </textarea>
                        <button className="comment-button" type="submit">Post</button>
                    </div>
                </form>
            </div>
        )
    }else if(option !== 'feed'){

        return (
            <div>
                <form onSubmit={handleSubmitProfile}>
                    <div className="comment-form-container">
                        <textarea
                            id={post.id}
                            className="comment-form-textarea"
                            cols="74"
                            placeholder="Add a comment..."
                            value={comment}
                            onChange={(e) => setComment(e.target.value)}
                        >
                        </textarea>
                        <button className="comment-button" type="submit">Post</button>
                    </div>

                </form>
            </div>

        )

    }

}


export default CommentForm;

// return (

//     <div>


//         {document.URL.includes(`http://localhost:3000/${currentUser.username}`) && document.URL.toString().length > 21 ?

//             <form onSubmit={handleSubmitProfile}>
//                 <div className="comment-form-container">
//                     <textarea
//                         id={post.id}
//                         className="comment-form-textarea"
//                         cols="74"
//                         placeholder="Add a comment..."
//                         value={comment}
//                         onChange={(e) => setComment(e.target.value)}
//                     >
//                     </textarea>
//                     <button className="comment-button" type="submit">Post</button>
//                 </div>

//             </form>
//             :

//             document.URL.toString().length === 22 ?

//                 <form onSubmit={handleSubmitDashboard}>
//                     <div className="comment-form-container">
//                         <textarea
//                             id={post.id}
//                             className="comment-form-textarea"
//                             cols="74"
//                             placeholder="Add a comment..."
//                             value={comment}
//                             onChange={(e) => setComment(e.target.value)}
//                         >
//                         </textarea>
//                         <button className="comment-button" type="submit">Post</button>
//                     </div>

//                 </form>

//                 :

//                 <form onSubmit={handleSubmitProfile}>
//                     <   div className="comment-form-container">
//                         <textarea
//                             id={post.id}
//                             className="comment-form-textarea"
//                             cols="74"
//                             placeholder="Add a comment..."
//                             value={comment}
//                             onChange={(e) => setComment(e.target.value)}
//                         >
//                         </textarea>
//                         <button className="comment-button" type="submit">Post</button>
//                     </div>

//                 </form>

//         }

//     </div>


// )
