from flask import Blueprint


article = Blueprint('article', __name__, url_prefix="/articles")
board = Blueprint('board', __name__, url_prefix="/boards")
category = Blueprint('category', __name__, url_prefix="/categories")
user = Blueprint('user', __name__, url_prefix="/users")
lst = Blueprint('list', __name__, url_prefix="/lists")

