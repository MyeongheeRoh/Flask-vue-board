from flask import Blueprint


article = Blueprint('article', __name__, url_prefix="/article")
board = Blueprint('board', __name__, url_prefix="/board")
category = Blueprint('category', __name__, url_prefix="/category")
user = Blueprint('user', __name__, url_prefix="/user")

