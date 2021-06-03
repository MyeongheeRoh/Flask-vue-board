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

class Comment(Base):
    __tablename__ = 't_comment'

    idSeq = Sequence('comment_seq', metadata = Base.metadata)
    commentId = Column('comment_id', Integer, idSeq, primary_key = True)
    articleId = Column('article_id', Integer, unique = False)
    userId = Column('user_id', Integer, unique = False)
    contents = Column('contents', String(50), unique = False)
    hidden = Column('hidden', Boolean, unique = False)
    isDeleted = Column('is_deleted', Boolean, unique = False)
    status = Column('status', String(10), unique = False)
    createdUser = Column('created_user', Integer, unique = False)
    createdAt = Column('created_at', DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = Column('modified_user', Integer, unique = False)
    modifiedAt = Column('modified_at', DateTime(timezone=True), server_default=func.now(), unique = False)

    def __init__(self, articleId, userId, contents):
        self.articleId = articleId
        self.userId = userId
        self.contents = contents

    def __repr__(self):
        return "<Comment %r %r %r %r %r %r %r %r %r %r %r>" % (self.commentId, self.articleId, self.userId,
            self.contents, self.isDeleted, self.hidden, self.status,
            self.createdUser, self.createdAt, self.modifiedUser, self.modifiedAt)

# Create tables.
Base.metadata.create_all(bind=engine)
