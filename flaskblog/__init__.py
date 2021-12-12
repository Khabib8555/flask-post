import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f40cf7d7ee3c763108c3f3b336e0e08c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ergashboevh@gmail.com'
app.config['MAIL_PASSWORD'] = 'bgqirnwycmvqtqmr'
mail = Mail(app)

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # for details open Lec23 slide 10
# app.config['MAIL_PASSWORD'] = 'your_app_password'  # for details open Lec23 slide 10
# app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'  # optional

from flaskblog import routes