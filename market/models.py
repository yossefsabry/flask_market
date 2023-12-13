# import models
from market import db, app
from sqlalchemy import inspect


# create class for user login
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=60), nullable=False ,unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)


    
# create class inhertance the features from db.moduel
# and create the column for the table


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))


    # this show the name in termainl  
    def __repr__(self):
        return f'Item {self.name}' # to show the the query by name



# make the table if not exist for change the table 
# with app.app_context():
#     inspector = inspect(db.engine)
    
#     # Check if the 'Item' table exists
#     if not inspector.has_table('item'):
#         db.create_all()

#     # Check if there is any data in the 'Item' table (unique)
#     if not Item.query.first():
#         # Add sample data
#         item1 = Item(name='Phone', price=500, barcode='893212299897', description='A smartphone')
#         item2 = Item(name='Laptop', price=900, barcode='123985473165', description='A laptop computer')
#         item3 = Item(name='Keyboard', price=150, barcode='231985128446', description='A computer keyboard')
#         item4 = Item(name='Gaming Keyborad', price=350, barcode='231985128123', description='A computer gaming keyboard')

#         # Add items to the session and commit
#         db.session.add_all([item1, item2, item3, item4])
#         db.session.commit()

# Now you can use the app with the existing database and data
