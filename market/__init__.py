from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# start config for the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# create secret key for the app most do it
app.config['SECRET_KEY'] = 'd65337e2c9b74480cc144ebf93b9d16711b106b9'

# app.config['CSRF_ENABLED'] = True
app.debug=True
# make instance from sqlalchemy class 
db = SQLAlchemy(app)

# start making bycrypt app for the password
bycript = Bcrypt(app)

# start login manager for the login page
login_manager = LoginManager(app)

# redirct login_requeried function to home page
login_manager.login_view = 'login_page'

# change the shape for login massage in login page for redirect 
login_manager.login_message_category = 'info'

from market import routes


