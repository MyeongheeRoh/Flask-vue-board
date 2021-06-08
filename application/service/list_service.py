from flask import Flask, g
from ..model.list import List


_list = List()

class List_service():
    
    def getListsList():
        try:
            lists = _list.select_all()
            return lists

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def getOneList(listId):
        try:
            list = _list.select_id(listId)
            return list

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def createList(data):
        try:
            newList = _list.create(data)
            return newList
        
        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e
            