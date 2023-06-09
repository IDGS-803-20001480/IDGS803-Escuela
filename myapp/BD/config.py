import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = 'SUPER_SECRET_KEY'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
   # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:"contraseña"@127.0.0.1:3306/idgs803'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Jonny25250509@127.0.0.1:3307/idgs803crud'
    SQLALCHEMY_TRACK_MODIFICATIONS = False