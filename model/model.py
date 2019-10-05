from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///milkstore.sqlite3'
app.config['SECRET_KEY'] = "abcdefgh"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Users()
class Users(db.Model):
    user_id = db.Column('user_id', db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column('First_Name', db.String(50))
    last_name = db.Column('Last_Name', db.String(50))
    email = db.Column('Email_ID', db.String(75), unique=True)
    password = db.Column('Password', db.String(50))
    is_admin = db.Column('Is_Admin', db.Boolean, unique=False, default=False)

class Products(db.Model):
    product_id = db.Column('Product_ID',db.Integer,primary_key=True)
    product_name = db.Column('Product_Name', db.String(50))
    unit_type = db.Column('Unit_type', db.String(50))
    product_description = db.Column('Product_Description',db.String(500))
    created_on = db.Column('Created_On',db.DateTime() , default = datetime.now())
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullable=False)
    modified_on = db.Column('Modified_On',db.DateTime(), default=datetime.now())
    modified_by = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullable=True)

class Supplier_Master(db.Model):
    supplier_id= db.Column('Supplier_ID', db.Integer, primary_key=True)
    first_name = db.Column('First_Name',db.String(25))
    last_name = db.Column('Last_Name', db.String(25))
    address = db.Column('Address',db.String(500))
    village = db.Column('Village', db.String(100))
    city = db.Column('City', db.String(50))
    state = db.Column('State', db.String(50))
    supplier_mobile = db.Column('Supplier_Mobile', db.Integer, unique=True)
    supplier_mobile2 = db.Column('Supplier_Mobile2', db.Integer)
    created_on = db.Column('Created_On',db.DateTime(), default=datetime.now())
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullable=False)
    modified_on = db.Column('Modified_On',db.DateTime(), default=datetime.now())
    modified_by = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullable=True)

class Purchase_Master(db.Model):
    purchase_id = db.Column('Purchase_ID', db.Integer, primary_key=True)
    supplier_id = db.Column('Supplier_ID', db.Integer, primary_key=True)
    product_id = db.Column('Product_ID', db.Integer, primary_key=True)
    purchase_qty = db.Column('Purchase_Qty', db.Integer)
    is_generated = db.Column('Is_Generated', db.Boolean, default=False)
    created_on = db.Column('Created_On', db.DateTime(),default=datetime.now())
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullable=False)
    modified_on = db.Column('Modified_On', db.DateTime(),default=datetime.now())
    modified_by = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullable=True)

# class Invoice_Master(db.Model):
#     invoice_id = db.Column('Invoice_ID', db.Integer, primary_key=True)
#
#
# class Ledger(db.Model):
#     pass
#
# class Invoice_Master(db.Model):
#     pass
#
# class Purchase_Details(db.Model):
#     pass