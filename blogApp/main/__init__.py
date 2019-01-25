from flask import Blueprint

bp = Blueprint('main', __name__)

from blogApp.main import routes