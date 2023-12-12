from flask import  Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# start config for the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'd65337e2c9b74480cc144ebf93b9d16711b106b9'
# make instance from sqlalchemy class 
db = SQLAlchemy(app)

from market import routes


