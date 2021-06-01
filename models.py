from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

engine = create_engine('postgresql://mae:mae1234@localhost:5432/test', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Article(db.Model):
    __tablename__ = 't_article'

    id_seq = Sequence('article_seq', metadata = Base.metadata)
    article_id = db.Column(db.Integer, primary_key = True)
    board_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    preface = db.Column(db.String(50))
    title = db.Column(db.String(50))
    contents = db.Column(db.String(50))
    liked = db.Column(db.Integer)
    is_auto_translation = db.Column(db.Boolean)
    is_fixed = db.Column(db.Boolean)
    is_slack_alarm = db.Column(db.Boolean)
    launch_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    is_deleted = db.Column(db.Boolean)
    hidden = db.Column(db.Boolean)
    created_user = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    modified_user = db.Column(db.Integer)
    modified_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, board_id, user_id, preface, title, contents, liked, is_auto_translation, 
                is_fixed, is_slack_alarm, launch_date, is_deleted, hidden, created_user, 
                created_at, modified_user, modified_at):
        self.article_id = article_id
        self.board_id = board_id
        self.user_id = user_id
        self.preface = preface
        self.title = title
        self.contents = contents
        self.liked = liked
        self.is_auto_translation = is_auto_translation
        self.is_fixed = is_fixed
        self.is_slack_alarm = is_slack_alarm
        self.launch_date = launch_date
        self.is_deleted = is_deleted
        self.hidden = hidden
        self.created_user = created_user
        self.created_at = created_at
        self.modified_user = modified_user
        self.modified_at = modified_at

    def __repr__(self):
        return "<User {self.nm}>"

# Create tables.
Base.metadata.create_all(bind=engine)
