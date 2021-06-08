from flask import Flask, render_template, redirect, request, g, Blueprint, url_for
from ..service.user_service import User_service
from ..board_blueprint import user


_user_service = User_service

# user Read
@user.route('/list')
def read():
    users = _user_service.getUsersList()
    print(users)
    return render_template('index.html', data = users)

# user Create
@user.route('/create')
def create():
    user_dict = {
        'name' : '홍길동'
    }
    _user_service.createUser(user_dict)
    return redirect(url_for('user.read'))