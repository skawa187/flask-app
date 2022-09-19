from . import db, login_mgr
from flask_login import UserMixin
import datetime

@login_mgr.user_loader
def load_user(id):
	return User.objects.get(id=id)

class User(db.Document, UserMixin):
	email = db.StringField(max_length=120, unique=True)
	f_name = db.StringField(max_length=120)
	l_name = db.StringField(max_length=120)
	password = db.StringField(max_length=100)

class Note(db.Document):
	title = db.StringField(max_length=100, required=True)
	content = db.StringField(max_length=20000)
	date = db.DateTimeField(default=datetime.datetime.utcnow)
	user_id = db.ObjectIdField()