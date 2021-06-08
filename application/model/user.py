from flask import g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import desc

from .. import db


class User(db.Model):
    __tablename__ = 't_user'

    idSeq = db.Sequence('user_seq', metadata = db.Model.metadata)
    userId = db.Column('user_id', db.Integer, idSeq, primary_key = True)
    name = db.Column('nm', db.String(45), unique = False)

    def select_all(self):
        users = User.query.order_by(desc(User.userId)).limit(5)
        
        return users

    def select_id(self, userId):
        user = User.query.filter_by(userId = userId)

        return user

    def create(self, data):
        newUser = User(
            name = data['name']
        )
        g.dao.add(newUser)
        g.dao.commit()

        return newUser

    def __repr__(self):
        return "<User %r %r>" % (self.userId, self.name)
