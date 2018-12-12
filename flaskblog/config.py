import os


class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+ os.environ.get('DATABASE_USER') + ':'+ os.environ.get('DATABASE_PASSWORD') + '@127.0.0.1:3306/flask?charset=utf8'

