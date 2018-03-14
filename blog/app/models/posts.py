from app.extensions import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    rid = db.Column(db.Integer, default=0)

    # 定义外键
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))



