from flask import Flask, request, flash, url_for, redirect, render_template,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_session import Session

app = Flask(__name__)
app.secret_key="Shivansh2021"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

Session(app)
db = SQLAlchemy(app)
app.app_context().push()

class contactquerys(db.Model):
   id = db.Column('query_id',db.Integer, primary_key=True)
   name=db.Column('query_name',db.String(30))    
   mobilenumber = db.Column('mobilenumber',db.Integer)
   email=db.Column('query_email',db.String(20))
   querytext=db.Column('querytext',db.String(150))
   creationdate=db.Column('creationdate',db.String(30))
   status=db.Column('status',db.String(30))
   closingdate=db.Column('closingdate',db.String(30))

   def __init__(self,name,mobilenumber,email,querytext,current_date,status,closingdate):
      self.name =name
      self.mobilenumber = mobilenumber
      self.email=email
      self.querytext=querytext
      self.creationdate= current_date
      self.status=status
      self.closingdate=closingdate      


@app.route('/')
def index():
   return render_template('index.html') 

@app.route('/SignIn')
def signIn():
   if session.get('logged_in')==True:
       return render_template('signIn.html',message = session['username'])
   else:
      return render_template('index.html' )   
   
@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      session['username'] = request.form['username']
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         session['logged_in'] = True
         return redirect(url_for('signIn',guest = 'Administrator'))
			
   return render_template('login.html', error = error)

@app.route('/product')
def product():
   if session.get('logged_in')==True:
      return render_template('product.html', guest = session['username'])
   else:
      return render_template('index.html' )                          


@app.route('/contactus', methods = ['GET', 'POST'])
def contact():
   if request.method == 'POST':
      current_datetime = datetime.now()
      formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
      contactquery = contactquerys(request.form['name'],request.form['mobile'],request.form['email'],request.form['querytext'],formatted_datetime,"Open","")
      db.session.add(contactquery)
      db.session.commit()
      flash('Record was successfully added')
      return redirect(url_for('output'))
   else:
      return render_template('contact.html')

@app.route('/output')
def output():
   return render_template('result1.html', contactquerys = contactquerys.query.all() )

@app.route('/bookmaid')
def maidbooking():
   return redirect('maidsummary')

@app.route('/maidsummary',methods=['GET', 'POST'])
def maidsummary():
   if request.method == 'POST':
      result = request.form
      return render_template('maidsummary.html',result=result)    
   else:
      return render_template('student.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)