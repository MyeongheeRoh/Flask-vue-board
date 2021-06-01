from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mae:mae1234@localhost:5432/test'

db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 't_article'

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


# readline_all.py
# f = open("article_data.txt", 'r')
# while True:
#     line = f.readline().strip('\n')
    
#     if not line: 
#         print('파일을 다읽었습니다.')
#         break

#     arr = line.split('\\')
#     print(arr)
#     article = Article(article_id = arr[0], board_id = arr[1], user_id = arr[2], preface = arr[3], title = arr[4], 
#     contents = arr[5], liked = arr[6], is_auto_translation = False, is_fixed = False, is_slack_alarm = False,
#     launch_date = arr[10], is_deleted = False, hidden = False, created_user = arr[13], created_at = arr[14], 
#     modified_user = arr[15], modified_at = arr[16])
#     print(article)
#     db.session.add(article)
#     db.session.commit()

# f.close()

#Article Read
@app.route('/')
def main():
    articles = db.session.query(Article).limit(5)

    return render_template('index.html', data = articles)

#Article Create
@app.route('/create', methods=['POST'])
def create():
    article = Article(article_id=100, board_id=1, title=request.form['title'], contents=request.form['contents'], user_id=request.form['userId'])
    db.session.add(article)
    db.session.commit()
    return redirect(url_for('main'))
