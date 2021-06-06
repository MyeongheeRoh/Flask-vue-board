from flask import Flask, render_template, redirect, request, g, Blueprint, url_for
from ..service.board_service import Board_service
from ..board_blueprint import board


_board_service = Board_service

# Board Read
@board.route('/list')
def read():
    boards = _board_service.getBoardsList()
    print(boards)
    return render_template('index.html', data = boards)

# Board Create
@board.route('/create')
def create():
    board_dict = {
        'name': '공지사항',
        'categoryId': 1,
        'likedFlag': False,
        'fileFlag': False,
        'commentFlag': False,
        'fixedFlag': False,
        'launchDateFlag': False,
        'langCount': 2,
        'langMode': 'kor',
        'accessAuth': 'admin',
        'hidden': False,
        'isDeleted': False,
    }
    _board_service.createBoard(board_dict)
    return redirect(url_for('board.read'))