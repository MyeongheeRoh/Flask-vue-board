from flask import Flask, g
from typing import Dict, Union
from ..model.article import Article

_article = Article()

class Article_service():
    
    def getArticlesList():
        try:
            articles = _article.select_all()
            return articles

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def getOneArticle(articleId):
        try:
            article = _article.select_id(articleId)
            return article

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def createArticle(data):
        try:
            newArticle = _article.create(data)
            return newArticle
        
        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e
            