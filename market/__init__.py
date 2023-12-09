from flask import  Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# start config for the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# make instance from sqlalchemy class 
db = SQLAlchemy(app)

from market import routes


