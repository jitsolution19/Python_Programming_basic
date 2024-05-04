from flask import Flask, request, flash, url_for, redirect, render_template, session
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_session import Session
from models.maidbooking import MaidBookings
from database import db

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

# Define Contact Query Model
class ContactQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    mobilenumber = db.Column(db.Integer)
    email = db.Column(db.String(20))
    querytext = db.Column(db.String(150))
    creationdate = db.Column(db.String(30))
    status = db.Column(db.String(30))
    closingdate = db.Column(db.String(30))

    def __init__(self, name, mobilenumber, email, querytext, current_date, status, closingdate):
        self.name = name
        self.mobilenumber = mobilenumber
        self.email = email
        self.querytext = querytext
        self.creationdate = current_date
        self.status = status
        self.closingdate = closingdate

# Define Routes
@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/product')
def product():
    if session.get('logged_in'):
        return render_template('product.html', guest=session['username'])
    else:
        return render_template('index.html')

@app.route('/contactus', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        with app.app_context():  # Ensure code is executed within application context
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
            contact_query = ContactQuery(
                request.form['name'],
                request.form['mobile'],
                request.form['email'],
                request.form['querytext'],
                formatted_datetime,
                "Open",
                ""
            )
            db.session.add(contact_query)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('output'))
    else:
        return render_template('contact.html')

@app.route('/output')
def output():
    with app.app_context():  # Ensure code is executed within application context
        contact_queries = ContactQuery.query.all()
    return render_template('result1.html', contact_queries=contact_queries)

# Define other routes...
@app.route('/bookmaid', methods = ['GET', 'POST'])
def maidbooking():
   if request.method == 'POST':
   #   result = request.form.to_dict()
   #   selections = request.form.getlist('category')
   #   result['category']=selections
     maidBooking = MaidBookings(request.form['Date'], request.form['timeslot'],"testing",request.form['customername'], request.form['housenum'], request.form['add1'], request.form['add2'], request.form['state'], request.form['district'])
     db.session.add(maidBooking)
     db.session.commit()
     flash('Record was successfully added')
     return redirect(url_for('maidsummary'))
   else:
    return render_template('student.html')

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
