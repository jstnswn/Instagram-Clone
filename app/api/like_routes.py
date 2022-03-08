from flask import Blueprint, jsonify, session, request
from flask_login import current_user
from app.models import User, Post, Comment, db, likes
from app.forms.post_form import PostForm


like_routes = Blueprint('like', __name__)


@like_routes.route('/', methods=['POST'])
def create_like():
    user_id = current_user.get_id()
    data = request.json
    user = User.query.get(user_id)
    post_id = data['post_id']

    post = Post.query.get(post_id)
    post.likers.append(user)

    db.session.commit()
    return {'user': user.f_to_dict()}, 200


@like_routes.route('/', methods=['DELETE'])
def delete_like():
    print('------------------')
    user_id = current_user.get_id()
    # user_id = 2
    data = request.json
    post_id = data['post_id']

    post = Post.query.get(post_id)
    print('------------------',user_id, post_id)
    # print('userID--------------',int(user_id))
    # print('post.likers[0].id------------------', post.likers[0].id)
    # print('-----------------------------',int(post.likers[0].id) == int(user_id))
    liker_to_delete = [user for user in post.likers if int(user.id) == int(user_id)][0]
    i = None
    for index, item in enumerate(post.likers):
        if int(item.id) == int(user_id):
            i = index
    # print('*******************',i)
    print('-------------------',liker_to_delete)
    print('----------------', post.likers)
    # like = likes.query.filter(likes.user_id == user_id)
    print('^^^^^^^^^^^^^^^^^^^^^^',likes)
    post.likers.remove(post.likers[i])
    print('--------------', post.likers)
    # db.session.add(post)
    db.session.commit()
    # return {'post': post.to_dict()}, 200
    return { 'message': 'success'}
