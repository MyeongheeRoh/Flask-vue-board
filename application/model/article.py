from sqlalchemy.sql import func
from . import Base
from app import db

class Article(Base):
    __tablename__ = 't_article'

    idSeq = db.Sequence('article_seq', metadata = Base.metadata)
    articleId = db.Column('article_id', db.Integer, idSeq, primary_key = True)
    boardId = db.Column('board_id', db.Integer, unique = False)
    userId = db.Column('user_id', db.Integer, unique = False)
    preface = db.Column('preface', db.String(50), unique = False)
    title = db.Column('title', db.String(50), unique = False)
    contents = db.Column('contents', db.String(50), unique = False)
    liked = db.Column('liked', db.Integer, unique = False)
    isAutoTranslation = db.Column('is_auto_translation', db.Boolean, unique = False)
    isFixed = db.Column('is_fixed', db.Boolean, unique = False)
    isSlackAlarm = db.Column('is_slack_alarm', db.Boolean, unique = False)
    launchDate = db.Column('launch_date', db.DateTime(timezone=True), server_default=func.now(), unique = False)
    isDeleted = db.Column('is_deleted', db.Boolean, unique = False)
    hidden = db.Column('hidden', db.Boolean, unique = False)
    createdUser = db.Column('created_user', db.Integer, unique = False)
    createdAt = db.Column('created_at', db.DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = db.Column('modified_user', db.Integer, unique = False)
    modifiedAt = db.Column('modified_at', db.DateTime(timezone=True), server_default=func.now(), unique = False)

    def __init__(self, boardId, userId, title, contents):
        self.boardId = boardId
        self.userId = userId
        self.title = title
        self.contents = contents

    def __repr__(self):
        return "<Article %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r>" % (self.articleId, self.boardId, self.userId, self.preface, self.title, 
            self.contents, self.liked, self.isAutoTranslation, self.isFixed, 
            self.isSlackAlarm, self.launchDate, self.isDeleted, self.hidden, 
            self.createdUser, self.createdAt, self.modifiedUser, self.modifiedAt)

# Create tables.
Base.metadata.create_all(bind=engine)
