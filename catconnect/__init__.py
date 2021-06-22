from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cat.db'
app.config['SECRET_KEY'] = 'ce2d1a413c1a28102085afeb'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from catconnect import routes