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

class Board(Base):
    __tablename__ = 't_board'

    idSeq = Sequence('board_seq', metadata = Base.metadata)
    boardId = Column('board_id', Integer, idSeq, primary_key = True)
    name = Column('nm', String(45), unique = False)
    categoryId = Column('category_id', Integer, idSeq, primary_key = True)
    likedFlag = Column('liked_flag', Boolean, unique = False)
    fileFlag = Column('file_flag', Boolean, unique = False)
    commentFlag = Column('comment_flag', Boolean, unique = False)
    fixedFlag = Column('fixed_flag', Boolean, unique = False)
    launchDateFlag = Column('launch_date_flag', Boolean, unique = False)
    langCount = Column('lang_count', Integer, idSeq, primary_key = True)
    langMode = Column('lang_mode', String(10), unique = False)
    accessAuth = Column('access_auth', String(10), unique = False)
    hidden = Column('hidden', Boolean, unique = False)
    isDeleted = Column('is_deleted', Boolean, unique = False)
    createdUser = Column('created_user', Integer, unique = False)
    createdAt = Column('created_at', DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = Column('modified_user', Integer, unique = False)
    modifiedAt = Column('modified_at', DateTime(timezone=True), server_default=func.now(), unique = False)

    def __init__(self, name, category_id):
        self.name = name
        self.categoryId = category_id

    def __repr__(self):
        return "<Board %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r>" % (self.boardId, self.name, self.categoryId, self.likedFlag, self.fileFlag, self.commentFlag, self.fixedFlag, self.launchDateFlag, self.langCount, self.langMode, self.accessAuth, self.hidden, self.isDeleted, self.createdUser, self.createdAt, self.modifiedUser, self.modifiedAt)

# Create tables.
Base.metadata.create_all(bind=engine)
