from flask import g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import desc

from . import Base
from .. import db


class Article(db.Model):
    __tablename__ = 't_article'

    idSeq = db.Sequence('article_seq', metadata = Base.metadata)
    articleId = db.Column('article_id', db.Integer, idSeq, primary_key = True)
    boardId = db.Column('board_id', db.Integer)
    userId = db.Column('user_id', db.Integer)
    preface = db.Column('preface', db.String(50))
    title = db.Column('title', db.String(50))
    contents = db.Column('contents', db.String(50))
    liked = db.Column('liked', db.Integer)
    isAutoTranslation = db.Column('is_auto_translation', db.Boolean, nullable=True)
    isFixed = db.Column('is_fixed', db.Boolean, nullable=True)
    isSlackAlarm = db.Column('is_slack_alarm', db.Boolean, nullable=True)
    launchDate = db.Column('launch_date', db.DateTime(timezone=True))
    isDeleted = db.Column('is_deleted', db.Boolean)
    hidden = db.Column('hidden', db.Boolean)
    createdUser = db.Column('created_user', db.Integer)
    createdAt = db.Column('created_at', db.DateTime(timezone=True), server_default=func.now())
    modifiedUser = db.Column('modified_user', db.Integer)
    modifiedAt = db.Column('modified_at', db.DateTime(timezone=True), server_default=func.now())

    # def __init__(self, boardId, userId, preface, title, contents, launchDate, liked=0, isAutoTranslation=False, isFixed=False, isSlackAlarm=False, isDeleted=False, hidden=False):
    #     self.boardId = boardId
    #     self.userId = userId
    #     self.preface = preface
    #     self.title = title
    #     self.contents = contents
    #     self.liked = liked
    #     self.isAutoTranslation = isAutoTranslation
    #     self.isFixed = isFixed
    #     self.isSlackAlarm = isSlackAlarm
    #     self.launchDate = launchDate
    #     self.isDeleted = isDeleted
    #     self.hidden = hidden

    def select_all(self):
        articles = Article.query.order_by(desc(Article.articleId)).limit(5)
        
        return articles

    def select_id(self, articleId):
        article = Article.query.filter_by(articleId = articleId)

        return article

    def create(self, data):
        newArticle = Article(
            boardId = data['boardId'],
            userId = data['userId'],
            preface = data['preface'],
            title = data['title'],
            contents = data['contents'],
            liked = data['liked'],
            isAutoTranslation = data['isAutoTranslation'],
            isFixed = data['isFixed'],
            isSlackAlarm = data['isSlackAlarm'],
            launchDate = data['launchDate'],
            isDeleted = data['isDeleted'],
            hidden = data['hidden']
        )
        g.dao.add(newArticle)
        g.dao.commit()

        return newArticle

    def __repr__(self):
        return "<Article %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r>" % (self.articleId, self.boardId, self.userId, self.preface, self.title, 
            self.contents, self.liked, self.isAutoTranslation, self.isFixed, 
            self.isSlackAlarm, self.launchDate, self.isDeleted, self.hidden, 
            self.createdUser, self.createdAt, self.modifiedUser, self.modifiedAt)
