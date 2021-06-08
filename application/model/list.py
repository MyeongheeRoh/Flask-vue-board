from flask import g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import desc

from .. import db


class List(db.Model):
    __tablename__ = 't_list'

    idSeq = db.Sequence('list_seq', metadata = db.Model.metadata)
    listId = db.Column('list_id', db.Integer, idSeq, primary_key = True)
    listCategoryId = db.Column('list_category_id', db.Integer, unique = False)
    korTitle = db.Column('kor_title', db.String(100), unique = False)
    jpTitle = db.Column('jp_title', db.String(100), unique = False)
    korPreface = db.Column('kor_preface', db.String(100), unique = False)
    jpPreface = db.Column('jp_preface', db.String(100), unique = False)
    writer = db.Column('writer', db.String(45), unique = False)
    korArticleId = db.Column('kor_article_id', db.Integer, unique = False)
    jpArticleId = db.Column('jp_article_id', db.Integer, unique = False)
    createdUser = db.Column('created_user', db.Integer, unique = False)
    createdAt = db.Column('created_at', db.DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = db.Column('modified_user', db.Integer, unique = False)
    modifiedAt = db.Column('modified_at', db.DateTime(timezone=True), server_default=func.now(), unique = False)

    def select_all(self):
        lists = List.query.order_by(desc(List.listId)).limit(5)
        
        return lists

    def select_id(self, listId):
        list = List.query.filter_by(listId = listId)

        return list

    def create(self, data):
        newList = List(
            listCategoryId = data['listCategoryId'],
            korTitle = data['korTitle'],
            jpTitle = data['jpTitle'],
            writer = data['writer'],
            korArticleId = data['korArticleId'],
            jpArticleId = data['jpArticleId']
        )
        g.dao.add(newList)
        g.dao.commit()

        return newList

    def __repr__(self):
        return "<List %r %r %r %r %r %r %r %r %r %r %r %r>" % (self.listId, self.listCategoryId,
            self.korTitle, self.jpTitle, self.writer, self.createdUser, self.createdAt, self.modifiedUser, 
            self.modifiedAt, self.korId, self.jpId)
