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

class User(Base):
    __tablename__ = 't_user'

    idSeq = Sequence('user_seq', metadata = Base.metadata)
    userId = Column('user_id', Integer, idSeq, primary_key = True)
    name = Column('nm', String(45), unique = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<User %r %r>" % (self.userId, self.name)

# Create tables.
Base.metadata.create_all(bind=engine)
