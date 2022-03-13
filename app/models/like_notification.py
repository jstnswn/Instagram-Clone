from sqlalchemy import ForeignKey
from .db import db
from datetime import datetime
# from .user import User
from .like import likes
class LikeNotification(db.Model):
    __tablename__ = 'like_notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_from_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_to_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    # is_checked = db.Column(db.Boolean, default=False)

    from_user = db.relationship('User', back_populates='l_from_notifications', viewonly=True, foreign_keys='LikeNotification.user_from_id')
    post = db.relationship('Post', back_populates='like_notifications')


    def to_dict(self):
        return {
            'id': self.id,
            'from_user': self.from_user.f_to_dict(),
            'post': self.post.n_to_dict(),
            # 'is_checked': self.is_checked
        }
