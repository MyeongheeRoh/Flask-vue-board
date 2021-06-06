from flask import Flask, render_template, redirect, request, g, Blueprint, url_for
from ..service.article_service import Article_service
from ..board_blueprint import article


_article_service = Article_service

# Article Read
@article.route('/list')
def read():
    articles = _article_service.getArticlesList()
    print(articles)
    return render_template('index.html', data = articles)

# Article Create
@article.route('/create')
def create():
    article_dict = {'boardId':1, 'userId':1, 'preface': '머릿말', 'title': '제목1', 'contents': '내용1', 'liked': 0, 'isAutoTranslation': False, 'isFixed': False, 'isSlackAlarm': False, 'launchDate': '2020-06-06', 'isDeleted': False, 'hidden': False}
    _article_service.createArticle(article_dict)
    return redirect(url_for('article.read'))

# Article Delete


# Article Update