''' 
models.py will define structure of database
'''

from blogApp import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
import jwt
from time import time
from flask import current_app
from blogApp.search import add_to_index, remove_from_index, query_index

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)



'''
Integrate search engine with SQLAlchemy

 a class method is a special method that is associated with the class and not a particular instance. 
'''
class SearchableMixin(object):

  '''
   search method wraps the query_index() function from app/search.py to replace the list of object IDs with actual objects.
  '''
  @classmethod
  def search(cls, expression, page, per_page):
    ids, total = query_index(cls.__tablename__, expression, page, per_page)
    if total == 0:
      return cls.query.filter_by(id = 0), 0
    when = []
    for i in range(len(ids)):
      when.append((ids[i], i))
    return cls.query.filter(cls.id.in_(ids)).order_by(db.case(when, value = cls.id)), total


  '''
  The method is to see what objects are going to be added, modified, deleted, available as session.new, session.dirty, session.deleted.
  These objects are not going to be available anymore after the session is committed, so I need to save them before the commit takes place.
  I'm using a session._changes dictionary to write these objects in a place that is going to survive the session commit, because as soon as the session is committed I will be using them to update the Elasticsearch index.
 '''
  @classmethod
  def before_commit(cls, session):
    session._changes = {
      'add': list(session.new),
      'update': list(session.dirty),
      'delete':list(session.deleted)
    }




  @classmethod
  def after_commit(cls, session):
    for obj in session._changes['add']:
      if isinstance(obj, SearchableMixin):
        add_to_index(obj.__tablename__, obj)
    for obj in session._changes['update']:
      if isinstance(obj, SearchableMixin):
        add_to_index(obj.__tablename__, obj)
    for obj in session._changes['delete']:
      if isinstance(obj, SearchableMixin):
        remove_from_index(obj.__tablename__, obj)
    session._changes = None


  '''
  The method is to refresh an index with all the data from the relational side.
  '''
  @classmethod
  def reindex(cls):
    for obj in cls.query:
      add_to_index(cls.__tablename__, obj)


db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)


class Post(SearchableMixin, db.Model):

    # any model that needs indexing needs to define a __searchable__ class attribute that lists the fields that need to be included in the index.
    __searchable__ = ['body']
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) # timestamp index post so can retrieve them in  chronological order.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5))
    def __repr__(self):
        return '<Post {}>'.format(self.body)

'''
 For the User model above, the corresponding table in the database will be named user. 
 For a AddressAndPhone model class, the table would be named address_and_phone.
 If you prefer to choose your own table names, you can add an attribute named __tablename__ to the model class, 
 set to the desired name as a string.
'''
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(64), index = True, unique = True)
  email = db.Column(db.String(120), index = True, unique = True)
  password_hash = db.Column(db.String(128))
  about_me = db.Column(db.String(140))
  last_seen = db.Column(db.DateTime, default=datetime.utcnow)

  '''
  For a one-to-many relationship, a db.relationship field is normally defined on the "one" side, and is used as a convenient way to get access to the "many". 
  The backref argument defines the name of a field that will be added to the objects of the "many" class that points back at the "one" object.
  '''
  posts = db.relationship('Post', backref='author', lazy='dynamic')


  '''
  The __repr__ method tells Python how to print objects of this class, which is going to be useful for debugging. 
  '''
  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  # generate avatar using gravatar
  def avatar(self, size):
    digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

  '''
  many to many relationship
  '''
  followed = db.relationship(
    'User', secondary=followers,
    primaryjoin=(followers.c.follower_id == id),
    secondaryjoin=(followers.c.followed_id == id),
    backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

  # handle follow functions
  def follow(self, user):
    if not self.is_following(user):
        self.followed.append(user)

  def unfollow(self, user):
    if self.is_following(user):
        self.followed.remove(user)

  def is_following(self, user):
    return self.followed.filter(
        followers.c.followed_id == user.id).count() > 0

  def followed_posts(self):
    followed = Post.query.join(
      followers, (followers.c.followed_id == Post.user_id)).filter(
        followers.c.follower_id == self.id)
    own = Post.query.filter_by(user_id=self.id)
    return followed.union(own).order_by(Post.timestamp.desc())


  # handle password reset from email

  # generates a JWT token as a string
  def get_reset_password_token(self, expires_in = 600): #expires in 10 min
    return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in}, current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

  # the method takes a token and attempts to decode, return user id if token is valid 
  @staticmethod  # static method does not receive class as first argument
  def verify_reset_password_token(token):
    try:
        id = jwt.decode(token, current_app.config['SECRET_KEY'],
                        algorithms=['HS256'])['reset_password']
    except:
        return
    return User.query.get(id)



'''
The user loader is registered with Flask-Login with the @login.user_loader decorator.
'''
@login.user_loader
def load_user(id):
    return User.query.get(int(id))




