from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, Boolean, DateTime
from sqlalchemy.sql import func

engine = create_engine('postgresql://mae:mae1234@localhost:5432/test', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Article(Base):
    __tablename__ = 't_article'

    idSeq = Sequence('article_seq', metadata = Base.metadata)
    articleId = Column('article_id', Integer, idSeq, primary_key = True)
    boardId = Column('board_id', Integer, unique = False)
    userId = Column('user_id', Integer, unique = False)
    preface = Column('preface', String(50), unique = False)
    title = Column('title', String(50), unique = False)
    contents = Column('contents', String(50), unique = False)
    liked = Column('liked', Integer, unique = False)
    isAutoTranslation = Column('is_auto_translation', Boolean, unique = False)
    isFixed = Column('is_fixed', Boolean, unique = False)
    isSlackAlarm = Column('is_slack_alarm', Boolean, unique = False)
    launchDate = Column('launch_date', DateTime(timezone=True), server_default=func.now(), unique = False)
    isDeleted = Column('is_deleted', Boolean, unique = False)
    hidden = Column('hidden', Boolean, unique = False)
    createdUser = Column('created_user', Integer, unique = False)
    createdAt = Column('created_at', DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = Column('modified_user', Integer, unique = False)
    modifiedAt = Column('modified_at', DateTime(timezone=True), server_default=func.now(), unique = False)

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
