import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):


  '''
  The value of the secret key is set as an expression with two terms, joined by the or operator. The first term looks for the value of an environment variable, also called SECRET_KEY. The second term, is just a hardcoded string. This is a pattern that you will see me repeat often for configuration variables. The idea is that a value sourced from an environment variable is preferred, but if the environment does not define the variable, then the hardcoded string is used instead. When you are developing this application, the security requirements are low, so you can just ignore this setting and let the hardcoded string be used. But when this application is deployed on a production server, I will be setting a unique and difficult to guess value in the environment, so that the server has a secure key that nobody else knows.
  '''
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


  '''
  In this case I'm taking the database URL from the DATABASE_URL environment variable, and if that isn't defined, I'm configuring a database named app.db located in the main directory of the application, which is stored in the basedir variable.
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False


  '''
  sending errors by email
  '''
  MAIL_SERVER = os.environ.get('MAIL_SERVER')
  MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
  MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  ADMINS = ['clu7sun@gmail.com']

  '''
  set to 3 for testing
  '''
  POSTS_PER_PAGE = 25


  LANGUAGES = ['en', 'zh']