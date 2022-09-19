from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

db = MongoEngine()
login_mgr = LoginManager()

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'dhsjakwqo isajdsja'
	app.config.from_envvar('FLASK_SETTINGS')

	db.init_app(app)

	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')

	from .models import User, Note


	login_mgr.login_view = 'auth.login'
	login_mgr.init_app(app)

	return app
