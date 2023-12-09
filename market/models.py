# import models
from market import db, app
from sqlalchemy import inspect

# create class inhertance the features from db.moduel
# and create the column for the table
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    # this show the name in termainl  
    def __repr__(self):
        return f'Item {self.name}'

# make the table if not exist for change the table 
with app.app_context():
    inspector = inspect(db.engine)
    
    # Check if the 'Item' table exists
    if not inspector.has_table('item'):
        db.create_all()

    # Check if there is any data in the 'Item' table (unique)
    if not Item.query.first():
        # Add sample data
        item1 = Item(name='Phone', price=500, barcode='893212299897', description='A smartphone')
        item2 = Item(name='Laptop', price=900, barcode='123985473165', description='A laptop computer')
        item3 = Item(name='Keyboard', price=150, barcode='231985128446', description='A computer keyboard')

        # Add items to the session and commit
        db.session.add_all([item1, item2, item3])
        db.session.commit()

# Now you can use the app with the existing database and data
