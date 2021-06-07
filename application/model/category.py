from flask import g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import desc

from . import Base
from .. import db

class Category(db.Model):
    __tablename__ = 't_category'

    idSeq = db.Sequence('category_seq', metadata = Base.metadata)
    categoryId = db.Column('category_id', db.Integer, idSeq, primary_key = True)
    name = db.Column('nm', db.String(45), unique = False)
    createdUser = db.Column('created_user', db.Integer, unique = False)
    createdAt = db.Column('created_at', db.DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = db.Column('modified_user', db.Integer, unique = False)
    modifiedAt = db.Column('modified_at', db.DateTime(timezone=True), server_default=func.now(), unique = False)

    def select_all(self):
        categories = Category.query.order_by(desc(Category.categoryId)).limit(5)
        
        return categories

    def select_id(self, categoryId):
        category = Category.query.filter_by(categoryId = categoryId)

        return category

    def create(self, data):
        newCategory = Category(
            name = data['name']
        )
        g.dao.add(newCategory)
        g.dao.commit()

        return newCategory

    def __repr__(self):
        return "<Category %r %r %r %r %r %r>" % (self.categoryId, self.name, self.createdUser, self.createdAt, self.modifiedUser, self.modifiedAt)
