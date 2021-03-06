from flask import render_template
from blogApp import db
from blogApp.errors import bp

@bp.errorhandler(404)
def not_found_error(error):
  return render_template('404.html'), 404

@bp.errorhandler(500)
def internal_error(error):
  db.session.rollback()
  return render_template('500.html'), 500