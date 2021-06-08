from flask import Flask, render_template, redirect, request, g, Blueprint, url_for
from ..service.list_service import List_service
from ..board_blueprint import lst


_list_service = List_service

# list Read
@lst.route('/list')
def read():
    lists = _list_service.getListsList()
    print(lists)
    return render_template('index.html', data = lists)

# list Create
# @list.route('/create')
# def create():
#     list_dict = {
#         'korTitle' : '안녕'
#         'jpTitle' : 'こんにちは'
#         'writer' : '홍길동'
#         'korArticleId' : 
#         'jpArticleId' : 
#     }
#     _list_service.createList(list_dict)
#     return redirect(url_for('list.read'))