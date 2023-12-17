# import models
from market import db, app, bycript, login_manager
# from sqlalchemy import inspect  #! if want ot add the the item by the code else leave like this
from flask_login import UserMixin #? some propertiues in the flask_login

# start login manager for he user loader for flask
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# create class for user login
class User(db.Model, UserMixin):
    """
    #? class user to store user in the database....
    """
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=60), nullable=False ,unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)
    
    # make property for budget
    @property
    def budget_prettier(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]}, {str(self.budget)[-3:]} $'
        else:
            return f'{self.budget}'
    # start attrabiutes for the password and the bycribt password
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        """
        #* to change the password to bycript password in the databasee....
        """
        self.password_hash = bycript.generate_password_hash(plain_text_password).decode('utf-8')
        
    def check_password_correction(self, attempted_password):
        """
        #? to check for the password after bycript in the login page and comppare with the database..
        """
        return bycript.check_password_hash(self.password_hash, attempted_password)
# create class inhertance the features from db.moduel
# and create the column for the table


class Item(db.Model):
    """
        #* class item its table in the database for 5 column the id name price barcode and description..
        #* and can add some relation between the user and item,,,
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))


    # this show the name in termainl  
    def __repr__(self):
        """
        #* to control to show the item in the database from termianl by name only 
        """
        return f'Item {self.name}' # to show the the query by name



# !! this code is to add the item by the vscode not terminal if want ot use it must add some changes in the code blow first

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
