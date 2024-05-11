from flask import Flask, request, flash, url_for, redirect, render_template, session
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_session import Session
from models.maidbooking import MaidBookings
from models.contactform import ContactQuery
from models.productInventory import ProductInventorys

from database import db
import json

app = Flask(__name__)
app.secret_key = "Shivansh2021"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy with the app
# db = SQLAlchemy(app)

# Initialize Flask Session
Session(app)
db.init_app(app)

# Define Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/SignIn')
def sign_in():
    if session.get('logged_in'):
        return render_template('signIn.html', message=session['username'])
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        session['username'] = request.form['username']
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            session['logged_in'] = True
            return redirect(url_for('sign_in', guest='Administrator'))

    return render_template('login.html', error=error)

@app.route('/product', methods = ['GET', 'POST'])
def product():
    if session.get('logged_in'):
        if request.method == 'POST':
            inventoryaddition = ProductInventorys(request.form['purchasedate'],request.form['productname'],request.form['productdescription'],request.form['productcategory'],request.form['productQuantity'],request.form['skunumber'],request.form['productimage'],request.form['productprice'],request.form['margin'],request.form['manufacturer'],request.form['seller'],request.form['location'])
            db.session.add(inventoryaddition)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('inventory'))
        else:            
            return render_template('product.html', guest=session['username'])
    else:
        return render_template('index.html')

@app.route('/inventory')
def inventory():
   return render_template('inventory1.html', ProductInventorys = ProductInventorys.query.all() )

@app.route('/contactus', methods = ['GET', 'POST'])
def contact():
   if request.method == 'POST':
      current_datetime = datetime.now()
      formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
      contactquery = ContactQuery(request.form['name'],request.form['mobile'],request.form['email'],request.form['querytext'],formatted_datetime,"Open","")
      db.session.add(contactquery)
      db.session.commit()
      flash('Record was successfully added')
      return redirect(url_for('output'))
   else:
      return render_template('contact.html')

@app.route('/output')
def output():
   return render_template('result1.html', contactquerys = ContactQuery.query.all() )

# Define other routes...
@app.route('/bookmaid', methods = ['GET', 'POST'])
def maidbooking():
   if request.method == 'POST':  
     categoryselections = request.form.getlist('category')
     categories_str = json.dumps(categoryselections)
     maidBooking = MaidBookings(request.form['Date'], request.form['timeslot'],categories_str,request.form['customername'], request.form['housenum'], request.form['add1'], request.form['add2'], request.form['state'], request.form['district'])
     db.session.add(maidBooking)
     db.session.commit()
     flash('Record was successfully added')
     return redirect(url_for('maidsummary'))
   else:
    return render_template('bookingMaid.html')

@app.route('/maidsummary')
def maidsummary():
      return render_template('maidsummary.html',maidBookings = MaidBookings.query.all())    

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    # Create all tables
    with app.app_context():  # Ensure code is executed within application context
        db.create_all()
    app.run(debug=True)
