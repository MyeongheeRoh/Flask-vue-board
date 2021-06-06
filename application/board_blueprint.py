from flask import Blueprint


article = Blueprint('article', __name__, url_prefix="/article")
board = Blueprint('board', __name__, url_prefix="/board")

