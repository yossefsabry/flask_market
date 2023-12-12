from market import app
from flask import render_template, redirect, url_for, request
from market.models import Item
from market.forms import RegisterFrom
from market import db
from market.models import User

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template("market.html" , items=items)



@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterFrom()
    
    if request.method == 'POST':
        if form.validate_on_submit(): # check on sumbit
            print("helllo______________________________________")
        try:
            create_user = User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data)
            db.session.add(create_user)
            db.session.commit()
            
        except Exception as e:
            print(f"Error creating user: {e}")
            return render_template("register.html", form=form)

        print("market page-----------------------")
        return redirect(url_for('market_page'))
        
    return render_template("register.html",  form=form)
