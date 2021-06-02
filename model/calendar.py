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

class Calendar(Base):
    __tablename__ = 't_calendar'

    idSeq = Sequence('calendar_seq', metadata = Base.metadata)
    calendarId = Column('article_id', Integer, idSeq, primary_key = True)
    title = Column('title', String(50), unique = False)
    startTime = Column('start_time', DateTime(timezone=True), server_default=func.now(), unique = False)
    endTime = Column('end_time', DateTime(timezone=True), server_default=func.now(), unique = False)
    isAllDay = Column('is_all_day', Boolean, unique = Flase)
    isSlackAlarm = Column('is_slack_alarm', Boolean, unique = False)
    category = Column('category', Integer, unique = False)
    isAutoTranslation = Column('is_auto_translation', Boolean, unique = False)
    contents = Column('contents', String(50), unique = False)
    isDeleted = Column('is_deleted', Boolean, unique = False)
    hidden = Column('hidden', Boolean, unique = False)
    createdUser = Column('created_user', Integer, unique = False)
    createdAt = Column('created_at', DateTime(timezone=True), server_default=func.now(), unique = False)
    modifiedUser = Column('modified_user', Integer, unique = False)
    modifiedAt = Column('modified_at', DateTime(timezone=True), server_default=func.now(), unique = False)

    def __init__(self, title, contents, startTime, endTime, category):
        self.title = title
        self.contents = contents
        self.startTime = startTime
        self.endTime = endTime
        self.category = category

    def __repr__(self):
        return "<Calendar %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r>" % (self.calendarId, self.title, self.startTime, self.endTime,
            self.isAllDay, self.isSlackAlarm, self.category,
            self.isAutoTranslation, self.contents, self.isDeleted, self.hidden, 
            self.createdUser, self.createdAt, self.modifiedUser, self.modifiedAt)

# Create tables.
Base.metadata.create_all(bind=engine)
