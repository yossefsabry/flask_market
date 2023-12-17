from wtforms import ValidationError
from market import app
from flask import render_template, redirect, url_for, request, flash, get_flashed_messages
from market.models import Item
from market.forms import RegisterFrom, login_from
from market import db
from market.models import User
from flask_login import login_user, current_user, logout_user, login_required
import email_validator

@app.route('/') # create route
@app.route('/home') 
def home_page(): # create the function for the routes
    """
    return: the home page info about the website...
    """
    return render_template("home.html") # render_template use to add a file html for this route

@app.route('/market')
@login_required
def market_page():
    """
    return: the market page for the product for the account
    """
    items = Item.query.all() # get all the item from the database
    return render_template("market.html" , items=items)



# ! there is an error in the code  "Exception: Install 'email_validator' for email validation support." in register >>>>>>> 
@app.route('/register', methods=['GET', 'POST']) # make the route methods accapt the post and get in the server
def register_page():
    """
    return: the register page for add a new user or sign in with an account
    """
    form = RegisterFrom() # create a instance from RegisterForm 
    
    if request.method == 'POST':
        if form.validate_on_submit(): # check on sumbit and vaildate for the inputs
            try:
                
                # Check if the username and email are unique
                form.vaildators_username(form.username)
                form.vaildators_email(form.email_address)

                create_user = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data) # create uesr to add for the database
                db.session.add(create_user)# add the new user
                db.session.commit() # push the new user

                login_user(current_user) #* bulid in function for login 
                flash("the account is created successfuly...", category="success")
                
            except ValidationError as e:
                print(f"Error creating user: {e}")
                flash(f"Validation Error: {e}", category="danger")
                return render_template("register.html", form=form)

            except Exception as e:
                print(f"Error creating user: {e}")
                db.session.rollback()  # Rollback the transaction
                flash("An error occurred while creating the user. Please try again.", category="danger")
                return render_template("register.html", form=form)

            
            return redirect(url_for('market_page')) # redirect its redirect for new route
    
    if form.errors != {} :
        for err_mas in form.errors.values():
            flash(f"the error: {err_mas}", category="danger") # use to show the errors in vaildation form in the base html(restor the error in flash)
            print(f"the error: {err_mas}") 
        
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    """
        reutrn: the login page ...
    """
    form = login_from()

    if form.validate_on_submit():
        print("hello".center(20, "*"))
        # ? add attemted_user to check if there any username with the same data in the data base
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            # ? if the user name in the database the password like the bycirpt password then can login
            login_user(attempted_user) #* bulid in function for login 
            flash("Success! you'r logged in...", category="success")
            return redirect(url_for('market_page'))
        else:
            # ? else there is an error
            flash("username and password not match! please try again", category="danger")
    return render_template('login.html' , form = form)

# start logout routes
@app.route("/logout")
def logout_page():
    logout_user()
    flash("you have been logout ...", category='info')
    return redirect(url_for('home_page'))