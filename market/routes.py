from market import app
from flask import render_template, redirect, url_for
from market.models import Item
from market.forms import RegisterFrom
from market import db
from market.models import User

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template("market.html" , items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterFrom()
    
    if form.is_submitted(): # check on sumbit
        
        create_user = User(username=form.username.data, email_address = form.email_address.data, password_hash = form.password1.data)
        
        db.session.add(create_user)
        db.session.commit()
        
        return redirect(url_for('market_page'))
    
    return render_template("register.html",  form=form)


