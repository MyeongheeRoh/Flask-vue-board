from flask import g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import desc

from . import Base
from .. import db


class Board(db.Model):
    __tablename__ = 't_board'

    idSeq = db.Sequence('board_seq', metadata = Base.metadata)
    boardId = db.Column('board_id', db.Integer, idSeq, primary_key = True)
    name = db.Column('nm', db.String(45), unique = False)
    categoryId = db.Column('category_id', db.Integer, idSeq, primary_key = True)
    likedFlag = db.Column('liked_flag', db.Boolean, unique = False)
    fileFlag = db.Column('file_flag', db.Boolean, unique = False)
    commentFlag = db.Column('comment_flag', db.Boolean, unique = False)
    fixedFlag = db.Column('fixed_flag', db.Boolean, unique = False)
    launchDateFlag = db.Column('launch_date_flag', db.Boolean, unique = False)
    langCount = db.Column('lang_count', db.Integer, idSeq, primary_key = True)
    langMode = db.Column('lang_mode', db.String(10), unique = False)
    accessAuth = db.Column('access_auth', db.String(10), unique = False)
    hidden = db.Column('hidden', db.Boolean, unique = False)
    isDeleted = db.Column('is_deleted', db.Boolean, unique = False)
    createdUser = db.Column('created_user', db.Integer, unique = False)
    createdAt = db.Column('created_at', db.DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = db.Column('modified_user', db.Integer, unique = False)
    modifiedAt = db.Column('modified_at', db.DateTime(timezone=True), server_default=func.now(), unique = False)
    
    def select_all(self):
        boards = Board.query.order_by(desc(Board.boardId)).limit(5)
        
        return boards

    def select_id(self, boardId):
        board = Board.query.filter_by(boardId = boardId)

        return board

    def create(self, data):
        newBoard = Board(
            name = data['name'],
            categoryId = data['categoryId'],
            likedFlag = data['likedFlag'],
            fileFlag = data['fileFlag'],
            commentFlag = data['commentFlag'],
            fixedFlag = data['fixedFlag'],
            launchDateFlag = data['launchDateFlag'],
            langCount = data['langCount'],
            langMode = data['langMode'],
            accessAuth = data['accessAuth'],
            hidden = data['hidden'],
            isDeleted = data['isDeleted']
        )
        g.dao.add(newBoard)
        g.dao.commit()

        return newBoard


    def __repr__(self):
        return "<Board %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r>" % (self.boardId, self.name, self.categoryId, self.likedFlag, self.fileFlag, self.commentFlag, self.fixedFlag, self.launchDateFlag, self.langCount, self.langMode, self.accessAuth, self.hidden, self.isDeleted, self.createdUser, self.createdAt, self.modifiedUser, self.modifiedAt)

