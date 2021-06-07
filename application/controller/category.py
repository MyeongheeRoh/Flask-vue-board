from flask import Flask, render_template, redirect, request, g, Blueprint, url_for
from ..service.category_service import Category_service
from ..board_blueprint import category


_category_service = Category_service

# category Read
@category.route('/list')
def read():
    categorys = _category_service.getCategorysList()
    print(categorys)
    return render_template('index.html', data = categorys)

# category Create
@category.route('/create')
def create():
    category_dict = {
        'name' : 'NEWS'
    }
    _category_service.createCategory(category_dict)
    return redirect(url_for('category.read'))