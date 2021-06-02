from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mae:mae1234@localhost:5432/test'

db = SQLAlchemy(app)

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
from model.article import Article

#Article Read
@app.route('/')
def main():
    articles = db.session.query(Article).limit(5)

    return render_template('index.html', data = articles)

#Article Create
@app.route('/create', methods=['POST'])
def create():
    article = Article(boardId=1, title=request.form['title'], contents=request.form['contents'], userId=request.form['userId'])
    db.session.add(article)
    db.session.commit()
    
    return redirect(url_for('main'))

# Default port:
if __name__ == '__main__':
    app.run()
