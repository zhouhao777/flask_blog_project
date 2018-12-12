import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ceshi123@127.0.0.1:3306/flask?charset=utf8'

