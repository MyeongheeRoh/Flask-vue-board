from flask import Flask, current_app

from .database import DBManager

app = Flask(__name__)

#애플리케이션 생성 함수
def create_app():

    print('*'*100)
    print('create app')
    print('*'*100)

    #기본 클래스와 설정 변경하기 위해 적용할 설정파일 설정
    from .config import Config
    app.config.from_object(Config)

    #db init
    with app.app_context():
        before_request()
    return app

@app.before_request
def before_request():
    db_url = app.config['SQLALCHEMY_DATABASE_URI']
    DBManager.init(db_url) #DB매니저 클래스 초기화
    DBManager.init_db()