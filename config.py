import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'ijdhf-iaal-siej-f95-1nm-dw012'

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = os.path.join(basedir, 'Movie_DB.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(basedir, 'Movie_DB.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

PER_PAGE = 21
