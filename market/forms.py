from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User
import email_validator

# create form
class RegisterFrom(FlaskForm):
    """
    # ? register form
    """
    # start check if the user in databasae or not
    def vaildators_username(self, username_to_create): # create func for collect the data for the username 
        user = User.query.filter_by(username=username_to_create.data).first() # filter by the name ot get the data
        if  user: # check for the user is true
            raise ValidationError('User Name Is Already Exists....')
    
    def vaildators_email(self, email_to_create):
        email = User.query.filter_by(email_address= email_to_create.data).first()
        if email:x
            raise ValidationError('Email Is Already Exists...')
    
    username = StringField(label="Username: ", validators=(Length(min=2, max=30), DataRequired()))
    email_address  = StringField(label="Email: ", validators=(Email(), DataRequired()))
    password1 = PasswordField(label="Password: ", validators=(Length(min=6), DataRequired()))
    password2 = PasswordField(label="Password Configuer: ", validators=(EqualTo('password1'), DataRequired()))
    
    submit = SubmitField(label="Create Acount")
    
    
    
class login_from(FlaskForm):
    """
    # ? login form..
    """
    username = StringField(label="Username: ", validators=(Length(min=2, max=30), DataRequired()))
    password = PasswordField(label="Password: ", validators=(Length(min=6), DataRequired()))    
    submit = SubmitField(label="Sign in")