[See original project](https://github.com/miguelgrinberg/microblog/tree/v0.4) - The tutorial by Miguel is awesome and interesting!!


# Tutorial Chapters:

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



# Extensions or tools:
1. **Flask-WTF** : thin wrapper around WTForms package. see Chapter 3.
2. **Flask-SQLAlchemy**: a Flask-friendly wrapper to the popular SQLAlchemy package, which is an Object Relational Mapper or ORM. ORMs allow applications to manage a database using high-level entities such as classes, objects and methods instead of tables and SQL. Supports  MySQL, PostgreSQL and SQLite. See Chapter 4.
3. **Flask-Migrate**: Address the problem of making updates to an existing databas.
	- `flask db init` create the migration repository.
	- `flask db migrate` sub-command generates these automatic migrations.  ie: `flask db migrate -m "users table"` detects and create user table
	- `flask db upgrade` apply the changes to the database
	- `flask db downgrade` undoes the last migration. 
4. [flask shell](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database): search flask shell to learn how to set up
```
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

```

5. **Werkzeug** password hashing
6. **Flask-Login**   manages the user logged-in state, so that for example users can log in to the application and then navigate to different pages while the application "remembers" that the user is logged in. 

7. Gravatar service
8. [Post/Redirect/Get](https://en.wikipedia.org/wiki/Post/Redirect/Get): The web development design prevents double form submission.
9.  **Flask-Mail** sending of emails
10. JSON Web Token, or JWT: Decode token :) => https://jwt.io/#debugger-io
11. Asychronous Emails

> What I really want is for the send_email() function to be asynchronous. What does that mean? It means that when this function is called, the task of sending the email is scheduled to happen in the background, freeing the send_email() to return immediately so that the application can continue running concurrently with the email being sent.


12. [OAuth](https://blog.miguelgrinberg.com/post/oauth-authentication-with-flask)
13. [Flask-Dance](https://github.com/singingwolfboy/flask-dance)
14. Bootstrap: CSS Framework, **flask-bootstrap**
15. **Moment.js**: a small open-source JavaScript library that takes date and time rendering to another level, as it provides every imaginable formatting option, and then some. **flask-moment**

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

16. **Flask-Babel** makes translation easy
17. [Single-page application](https://en.wikipedia.org/wiki/Single-page_application): a web application or web site that interacts with the user by dynamically rewriting the current page rather than loading entire new pages from a server. Tools to achieve SPA includes Javascript, Ajax etc. . In JavaScript there is no such thing as waiting for something, everything is asynchronous.  JavaScript works a lot with callback functions, or a more advanced form of callbacks called promises. 
18. **guess_language**: determine the language being used

# How to run the app locally
```
cd simple-flask-heroku
virtualenv venv
. venv/bin/activate
export FLASK_APP=microblog.py 
export FLASK_ENV=development
flask run
```

