from flask import Flask,render_template,redirect,url_for,request,flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from datetime import datetime

app = Flask(__name__)
app.secret_key="Shivansh2021"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///D:/Pre%20Bill/FlaskProject/datbase.db'
Session(app)
db = SQLAlchemy(app)

class contactquery(db.Model):
   id = db.Column('query_id',db.Integer, primary_key=True)
   name=db.Column('query_name',db.String(30)) 
   mobilenumber = db.Column('mobilenumber',db.Integer)
   email=db.Column('query_email',db.String(20))
   query=db.Column('querytext',db.String(150))
   creationdate=db.Column('creationdate',db.String(30))
   status=db.Column('status',db.String(30))
   closingdate=db.Column('closingdate',db.String(30))
   
def __init__(self,name,mobilenumber,email,query):
   self.name =name
   self.mobilenumber=mobilenumber
   self.email=email
   self.query=query
   current_datetime = datetime.now()
   current_date = current_datetime.date()
   self.creationdate= current_date
     

@app.route('/')
def index():
   return render_template('index.html') 

@app.route('/bookmaid')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
   else:
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


@app.route('/contact')
def contact():
   if request.method == 'POST':
      contact = contactquery(request.form['name'],request.form['mobilenumber'],request.form['email'],request.form['query'])
      db.session.add(contact)
      db.session.commit()
      flash('Record was successfully added')
      return redirect(url_for('showall'))
   else:
      return render_template('contact.html')

@app.route('/showall')
def showall():
   return render_template('show_all.html', contact = contactquery.query.all() )

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

# @app.route('/')
# def index():
#    return '<html><body><h1>Hello World</h1></body></html>'

# @app.route('/users/<username>')
# def hellouser(username):
#    if username =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = username))
   
if __name__ == '__main__':
   app.run(debug = True)