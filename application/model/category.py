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

class Category(Base):
    __tablename__ = 't_category'

    idSeq = Sequence('category_seq', metadata = Base.metadata)
    categoryId = Column('category_id', Integer, idSeq, primary_key = True)
    name = Column('nm', String(45), unique = False)
    createdUser = Column('created_user', Integer, unique = False)
    createdAt = Column('created_at', DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = Column('modified_user', Integer, unique = False)
    modifiedAt = Column('modified_at', DateTime(timezone=True), server_default=func.now(), unique = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category %r %r %r %r %r %r>" % (self.categoryId, self.name, self.createdUser, self.createdAt, self.modifiedUser, self.modifiedAt)

# Create tables.
Base.metadata.create_all(bind=engine)
