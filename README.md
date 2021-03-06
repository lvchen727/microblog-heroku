[See original project](https://github.com/miguelgrinberg/microblog/tree/v0.4) - The tutorial by Miguel is awesome and interesting!!

[**See my version of microblog app deployed on heroku**](https://microblog-clu.herokuapp.com/auth/login?next=%2F)


## Tutorial Chapters:

1. [Hello world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
2. [Template](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
3. [Web forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
4. [Database](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
5. [Users Login](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
6. [Profile Page and Avatars](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars)
7. [Error handling](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling)
8. [Pagination](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)
9. [Email Support](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)
10. [OAuth](https://blog.miguelgrinberg.com/post/oauth-authentication-with-flask)
	[see template example about OAuth](https://github.com/miguelgrinberg/flask-oauth-example)
11. [Facelift](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift)
12. [Dates and Time](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xii-dates-and-times)
13. [Flask-Babel](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
14. [Ajax](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-ajax)
15. [Better App structure](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)

      Try to restructure the codes in a way"
      * repack codes into modules so that we could reuse them for later projects
      * Use application factory, so we could initiate different application instances for testing

16. [Full text search](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search)
17. [Deploy on Heroku](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku)




## Extensions or tools:
* **Flask-WTF** : thin wrapper around WTForms package. see Chapter 3.
* **Flask-SQLAlchemy**: a Flask-friendly wrapper to the popular SQLAlchemy package, which is an Object Relational Mapper or ORM. ORMs allow applications to manage a database using high-level entities such as classes, objects and methods instead of tables and SQL. Supports  MySQL, PostgreSQL and SQLite. See Chapter 4.
* **Flask-Migrate**: Address the problem of making updates to an existing databas.
	- `flask db init` create the migration repository.
	- `flask db migrate` sub-command generates these automatic migrations.  ie: `flask db migrate -m "users table"` detects and create user table
	- `flask db upgrade` apply the changes to the database
	- `flask db downgrade` undoes the last migration. 
* [flask shell](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database): search flask shell to learn how to set up
```
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

```

* **Werkzeug** password hashing
* **Flask-Login**   manages the user logged-in state, so that for example users can log in to the application and then navigate to different pages while the application "remembers" that the user is logged in. 

* Gravatar service
* [Post/Redirect/Get](https://en.wikipedia.org/wiki/Post/Redirect/Get): The web development design prevents double form submission.
*  **Flask-Mail** sending of emails
* JSON Web Token, or JWT: Decode token :) => https://jwt.io/#debugger-io
* Asychronous Emails

> What I really want is for the send_email() function to be asynchronous. What does that mean? It means that when this function is called, the task of sending the email is scheduled to happen in the background, freeing the send_email() to return immediately so that the application can continue running concurrently with the email being sent.


* [OAuth](https://blog.miguelgrinberg.com/post/oauth-authentication-with-flask)
* [Flask-Dance](https://github.com/singingwolfboy/flask-dance)
* Bootstrap: CSS Framework, **flask-bootstrap**
* **Moment.js**: a small open-source JavaScript library that takes date and time rendering to another level, as it provides every imaginable formatting option, and then some. **flask-moment**

```
moment('2017-09-28T21:45:23Z').format('L')
"09/28/2017"
moment('2017-09-28T21:45:23Z').format('LL')
"September 28, 2017"
moment('2017-09-28T21:45:23Z').format('LLL')
"September 28, 2017 2:45 PM"
moment('2017-09-28T21:45:23Z').format('LLLL')
"Thursday, September 28, 2017 2:45 PM"
moment('2017-09-28T21:45:23Z').format('dddd')
"Thursday"
moment('2017-09-28T21:45:23Z').fromNow()
"7 hours ago"
moment('2017-09-28T21:45:23Z').calendar()
"Today at 2:45 PM"
```

* **Flask-Babel** makes translation easy
* [Single-page application](https://en.wikipedia.org/wiki/Single-page_application): a web application or web site that interacts with the user by dynamically rewriting the current page rather than loading entire new pages from a server. Tools to achieve SPA includes Javascript, Ajax etc. . In JavaScript there is no such thing as waiting for something, everything is asynchronous.  JavaScript works a lot with callback functions, or a more advanced form of callbacks called promises. 
* **guess_language**: determine the language being used

* **Full text search engines supported by Flask**

Support for full-text search is not standardized like relational databases are. There are several open-source full-text engines: Elasticsearch, Apache Solr, Whoosh, Xapian, Sphinx, etc. As if this isn't enough choice, there are several databases that also provide searching capabilities that are comparable to dedicated search engines like the ones I enumerated above. SQLite, MySQL and PostgreSQL all offer some support for searching text, and NoSQL databases such as MongoDB and CouchDB do too.

- [Elasticsearch engine installation](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/docker.html)


## Deploy on Heroku


####  1. create app `flask-microblog`
`heroku apps:create flask-microblog`

####  2. verify app
`git remote -v`

####  3. Working with a Heroku Postgres Database
`heroku addons:add heroku-postgresql:hobby-dev`

####  4. logging to stdout(required by heroku)
// modify __init__.py and config.py

```
class Config(object):
    # ...
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
```

```
def create_app(config_class=Config):
    # ...
    if not app.debug and not app.testing:
        # ...

        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/microblog.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')

    return app
```


`heroku config:set LOG_TO_STDOUT=1`

####  5. Elasticsearch Hosting
```
heroku addons:create searchbox:starter
heroku config:get SEARCHBOX_URL
heroku config:set ELASTICSEARCH_URL=<your-elasticsearch-url>
```

####  6. Update requirements with `gunicorn` and `psycopg2`

####  7. Procfile
Heroku needs to know how to execute the application, and for that it uses a file named Procfile in the root directory of the application. The format of this file is simple, each line includes a process name, a colon, and then the command that starts the process. 

```
web: flask db upgrade; flask translate compile; gunicorn microblog:app
```

####  8. Add configuration

Because first two commands in Procfile are based on flask commands, I need to set FLASK_APP env variable

` heroku config:set FLASK_APP=microblog.py`

####  9. Deploy the App

```
git commit -a -m "heroku deployment changes"
git push heroku deploy:master

```

#### 10. Deploying Application Updates

Just commit and push again!


## How to run the app locally
```
cd microblog-heroku
virtualenv venv
. venv/bin/activate
export FLASK_APP=microblog.py 
export FLASK_ENV=development
flask run
```

## Other heroku deployment tutorial

[deploy app to heroku](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0)
