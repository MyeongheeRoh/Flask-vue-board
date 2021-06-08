from flask import Flask, g
from ..model.user import User


_user = User()

class User_service():
    
    def getUsersList():
        try:
            users = _user.select_all()
            return users

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def getOneUser(userId):
        try:
            user = _user.select_id(userId)
            return user

        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e

    def createUser(data):
        try:
            newUser = _user.create(data)
            return newUser
        
        except Exception as e:
            print('!'*100)
            print('error message:',e)
            raise e
            