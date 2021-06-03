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

class File(Base):
    __tablename__ = 't_file'

    idSeq = Sequence('file_seq', metadata = Base.metadata)
    fileId = Column('file_id', Integer, idSeq, primary_key = True)
    articleId = Column('article_id', Integer, unique = False)
    fileName = Column('file_nm', String(36), unique = False)
    originFileName = Column('origin_file_nm', String(260), unique = False)
    filePath = Column('file_path', String(500), unique = False)
    fileExtention = Column('file_extension', String(12), unique = False)
    isDeleted = Column('is_deleted', Boolean, unique = False)
    status = Column('status', String(10), unique = False)
    createdUser = Column('created_user', Integer, unique = False)
    createdAt = Column('created_at', DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = Column('modified_user', Integer, unique = False)
    modifiedAt = Column('modified_at', DateTime(timezone=True), server_default=func.now(), unique = False)

    def __init__(self, articleId, originFileName):
        self.articleId = articleId
        self.originFileName = originFileName

    def __repr__(self):
        return "<File %r %r %r %r %r %r %r %r %r %r %r %r>" % (self.fileId, self.articleId, self.fileName,
            self.originFileName, self.filePath, self.fileExtention, self.isDeleted, self.status,
            self.createdUser, self.createdAt, self.modifiedUser, self.modifiedAt)

# Create tables.
Base.metadata.create_all(bind=engine)
