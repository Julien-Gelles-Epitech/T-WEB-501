import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt

from flask_login import LoginManager

app = Flask(__name__)

## app.config

app.config['SECRET_KEY'] = "FyKQw   }QMjrr{tYs-8`c"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

lm = LoginManager()
lm.init_app(app)

from Flask_server import routes