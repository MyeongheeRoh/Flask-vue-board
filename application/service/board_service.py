from flask import Flask, g
from typing import Dict, Union
from ..model.board import Board


_board = Board()

class Board_service():
    
    def getBoardsList():
        try:
            boards = _board.select_all()
            return boards

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def getOneBoard(boardId):
        try:
            board = _board.select_id(boardId)
            return board

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def createBoard(data):
        try:
            newBoard = _board.create(data)
            return newBoard
        
        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e
            