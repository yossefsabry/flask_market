from flask import  Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# start config for the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# make instance from sqlalchemy class 
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

    

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template("market.html" , items=items)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
