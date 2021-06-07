from flask import Flask, g
from ..model.category import Category


_category = Category()

class Category_service():
    
    def getCategorysList():
        try:
            categorys = _category.select_all()
            return categorys

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def getOneCategory(categoryId):
        try:
            category = _category.select_id(categoryId)
            return category

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def createCategory(data):
        try:
            newCategory = _category.create(data)
            return newCategory
        
        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e
            