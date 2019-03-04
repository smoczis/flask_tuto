import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "ROMEUSZ"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.poczta.interia.pl'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 465
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'roman.owski@interia.pl'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'przeginiaduchowna336'

    POSTS_PER_PAGE = 5
    LANGUAGES = ['en', 'pl']
