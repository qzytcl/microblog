import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir,'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	ADMINS = ['876325461@qq.com']
	POSTS_PER_PAGE = 20
	DEBUG = True
	LANGUAGES = ['zh_Hans_CN','en']
	MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY') or '20190905000332169'
	ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')