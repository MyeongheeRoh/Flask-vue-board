from sqlalchemy.ext.declarative import declarative_base #declarative 선언자 모듈
Base = declarative_base()

__all__ = ['article', 'board', 'calendar', 'category', 'comment', 'file', 'list', 'user']