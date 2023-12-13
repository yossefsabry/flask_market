from market import app
from flask import render_template, redirect, url_for, request, flash, get_flashed_messages
from market.models import Item
from market.forms import RegisterFrom
from market import db
from market.models import User

@app.route('/') # create route
@app.route('/home') 
def home_page(): # create the function for the routes
    """
    the home page info about the website...
    """
    return render_template("home.html") # render_template use to add a file html for this route

@app.route('/market')
def market_page():
    """
    the market page for the product for the account
    """
    items = Item.query.all() # get all the item from the database
    return render_template("market.html" , items=items)



@app.route('/register', methods=['GET', 'POST']) # make the route methods accapt the post and get in the server
def register_page():
    """
    the register page for add a new user or sign in with an account
    """
    form = RegisterFrom() # create a instance from RegisterForm 
    
    if request.method == 'POST':
        if form.validate_on_submit(): # check on sumbit
            try:
                create_user = User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data) # create uesr to add for the database
                db.session.add(create_user)# add the new user
                db.session.commit() # push the new user
                
            except Exception as e:
                print(f"Error creating user: {e}")
                return render_template("register.html", form=form)

            return redirect(url_for('market_page')) # redirect its redirect for new route
    
    if form.errors != {} :
        for err_mas in form.errors.values():
            flash(f"the error: {err_mas}", category="danger") # use to show the errors in vaildation form in the base html(restor the error in flash)
            print(f"the error: {err_mas}") 
        
    return render_template("register.html", form=form)
