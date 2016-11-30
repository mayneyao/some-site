from . import db
from flask import url_for
from flask.ext.login import UserMixin,login_user,LoginManager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from . import  login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class Email(db.Model):
#     __tablename__ = 'od_email'
#     id = db.Column(db.Integer,primary_key=True)
#     email = db.Column(db.String(64),unique=True,index=True)

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    # role_id = db.
    # posts = db.relationship('Post',backref='author',lazy='dynamic')

class Post(db.Model):
    __tablename__= 'posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    tag = db.Column(db.String(64))
    content = db.Column(db.Text)
    subtime = db.Column(db.DateTime,index=True,default=datetime.now())

    @staticmethod
    def fakepage(count=100):
        from random import seed,randint
        import forgery_py
        seed()
        for i in range(count):
            p = Post(title = "testpage"+str(randint(1,100)),content = forgery_py.lorem_ipsum.sentence())
            db.session.add(p)
            db.session.commit()
    # author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    def to_json(self):
        json_post = {
            'url': url_for('api.get_post', id=self.id, _external=True),
            'title': self.title,
            'content': self.content,
            'subtime': self.subtime
        }
        return json_post
#
# class Role(db.Model):
#     __tablename__= 'roles'
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(64),unique=True)
#     default =  db.Column(db.Boolean,default=False,index=True)
#     permissions = db.Column(db.Integer)
