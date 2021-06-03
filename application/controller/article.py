from flask import render_template, redirect, request
from ..model.article import Article

#Article Read
@app.route('/')
def main():
    articles = dao.query(Article).limit(5)

    return render_template('index.html', data = articles)

#Article Create
@app.route('/create', methods=['POST'])
def create():
    article = Article(boardId=1, title=request.form['title'], contents=request.form['contents'], userId=request.form['userId'])
    dao.add(article)
    dao.commit()
    
    return redirect(url_for('main'))