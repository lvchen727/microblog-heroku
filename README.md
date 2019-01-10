[See original project](https://github.com/miguelgrinberg/microblog/tree/v0.4)


# Tutorial Chapters:

1. [Hello world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
2. [Template](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
3. [Web forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
4. [Database](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
5. [Users Login](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
6. [Profile Page and Avatars](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars)
7. [Error handling](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling)

# Extensions or tools:
1. **Flask-WTF** : thin wrapper around WTForms package. see Chapter 3.
2. **Flask-SQLAlchemy**: a Flask-friendly wrapper to the popular SQLAlchemy package, which is an Object Relational Mapper or ORM. ORMs allow applications to manage a database using high-level entities such as classes, objects and methods instead of tables and SQL. Supports  MySQL, PostgreSQL and SQLite. See Chapter 4.
3. **Flask-Migrate**: Address the problem of making updates to an existing databas.
	- `flask db init` create the migration repository.
	- `flask db migrate` sub-command generates these automatic migrations.  ie: `flask db migrate -m "users table"` detects and create user table
	- `flask db upgrade` apply the changes to the database
	- `flask db downgrade` undoes the last migration. 
4. flask shell 
5. **Werkzeug** password hashing
6. **Flask-Login**   manages the user logged-in state, so that for example users can log in to the application and then navigate to different pages while the application "remembers" that the user is logged in. 

7. Gravatar service






