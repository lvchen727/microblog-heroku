''' 
models.py will define structure of database
'''

from blogApp import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

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


  def avatar(self, size):
      digest = md5(self.email.lower().encode('utf-8')).hexdigest()
      return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) # timestamp index post so can retrieve them in  chronological order.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)



'''
The user loader is registered with Flask-Login with the @login.user_loader decorator.
'''
@login.user_loader
def load_user(id):
    return User.query.get(int(id))