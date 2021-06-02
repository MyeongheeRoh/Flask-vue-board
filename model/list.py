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

class List(Base):
    __tablename__ = 't_list'

    idSeq = Sequence('list_seq', metadata = Base.metadata)
    listId = Column('list_id', Integer, idSeq, primary_key = True)
    listCategoryId = Column('list_category_id', Integer, unique = False)
    korTitle = Column('kor_title', String(100), unique = False)
    jpTitle = Column('jp_title', String(100), unique = False)
    writer = Column('writer', String(45), unique = False)
    createdUser = Column('created_user', Integer, unique = False)
    createdAt = Column('created_at', DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = Column('modified_user', Integer, unique = False)
    modifiedAt = Column('modified_at', DateTime(timezone=True), server_default=func.now(), unique = False)
    korId = Column('kor_id', Integer, unique = False)
    jpId = Column('jp_id', Integer, unique = False)

    def __init__(self, listId, listCategoryId, korTitle, jpTitle, writer):
        self.listId = listId
        self.listCategoryId = listCategoryId
        self.korTitle = korTitle
        self.jpTitle = jpTitle
        self.writer = writer

    def __repr__(self):
        return "<List %r %r %r %r %r %r %r %r %r %r %r %r>" % (self.listId, self.listCategoryId,
            self.korTitle, self.jpTitle, self.writer, self.createdUser, self.createdAt, self.modifiedUser, 
            self.modifiedAt, self.korId, self.jpId)

# Create tables.
Base.metadata.create_all(bind=engine)
