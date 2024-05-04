from flask import Flask,render_template,redirect,url_for,request,flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from datetime import datetime

app = Flask(__name__)
app.secret_key="Shivansh2021"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///D:/Pre%20Bill/FlaskProject/datbase.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Pre%20Bill/FlaskProject/Python_Programming_basic/Website/testingdata.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# sqlite:///example.db
# Session(app)
db = SQLAlchemy(app)
app.app_context().push()

# class students(db.Model):
#    id = db.Column('student_id', db.Integer, primary_key = True)
#    name = db.Column(db.String(100))
#    city = db.Column(db.String(50))
#    addr = db.Column(db.String(200)) 
#    pin = db.Column(db.String(10))

#    def __init__(self, name, city, addr,pin):
#     self.name = name
#     self.city = city
#     self.addr = addr
#     self.pin = pin


class contactquerys(db.Model):
   id = db.Column('query_id',db.Integer, primary_key=True)
   name=db.Column('query_name',db.String(30)) 
   mobilenumber = db.Column('mobilenumber',db.Integer)
   email=db.Column('query_email',db.String(20))
   query=db.Column('querytext',db.String(30))
   creationdate=db.Column('creationdate',db.String(30))
   status=db.Column('status',db.String(30))
   closingdate=db.Column('closingdate',db.String(30))
   
   def __init__(self,name,mobilenumber,email,query,current_date,status,closingdate):
      self.name =name
      self.mobilenumber=mobilenumber
      self.email=email
      self.query=query
      self.creationdate= current_date
      self.status=status
      self.closingdate=closingdate

# class tempquerys(db.Model):
#    id = db.Column('query_id',db.Integer, primary_key=True)
#    name=db.Column('query_name',db.String(30)) 
#    mobilenumber = db.Column('mobilenumber',db.Integer)
#    email=db.Column('query_email',db.String(20))
#    query=db.Column('querytext',db.String(150))
#    creationdate=db.Column('creationdate',db.String(30))
   
#    def __init__(self,name,mobilenumber,email,query,current_date):
#       self.name =name
#       self.mobilenumber=mobilenumber
#       self.email=email
#       self.query=query
#       self.creationdate= current_date

# class TempUser(db.Model):
#    id = db.Column('userid',db.Integer, primary_key=True)
#    username=db.Column('username',db.String(30))    
#    def __init__(self,username):
#       self.username = username



@app.route('/')
def index():
   return render_template('index.html') 

# @app.route('/jituser')
# def jituser():  
#       return render_template('shiv.html')

# @app.route('/jitresult',methods=['GET', 'POST'])
# def jitresult():
#     if request.method == 'POST':
#       # gupta = request.form
#       aka = TempUser(request.form['username'])
#       print(aka.username)
#       db.session.add(aka)
#       db.session.commit()
#       flash('Record was successfully added')
#       return render_template("shiv2.html",students = aka.username)
      # aka = TempUser(request.form['username'])
      # db.session.add(aka)
      # db.session.commit()
      # akauser=request.form
      # flash('Record was successfully added')
   #    # return render_template('shiv2.html',akauser=akauser)
   #  else:       
   #    return render_template('shiv2.html',students = "testing")

# @app.route('/bookmaid')
# def student():
#    return render_template('student.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)
#    else:
#       return render_template('index.html')

# @app.route('/SignIn')
# def signIn():
#    if session.get('logged_in')==True:
#        return render_template('signIn.html',message = session['username'])
#    else:
#       return render_template('index.html' )    
  

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#    error = None
   
#    if request.method == 'POST':
#       session['username'] = request.form['username']
#       if request.form['username'] != 'admin' or \
#          request.form['password'] != 'admin':
#          error = 'Invalid username or password. Please try again!'
#       else:
#          flash('You were successfully logged in')
#          session['logged_in'] = True
#          return redirect(url_for('signIn',guest = 'Administrator'))
			
#    return render_template('login.html', error = error)

# @app.route('/product')
# def product():
#    if session.get('logged_in')==True:
#       return render_template('product.html', guest = session['username'])
#    else:
#       return render_template('index.html' )                          

@app.route('/showall')
def showall():
      return render_template('result1.html', contactquerys = contactquerys.query.all())


@app.route('/contact',methods=['GET', 'POST'])
def contact():
   if request.method == 'POST':
      contactquery = contactquerys(request.form['name'],request.form['mobile'],request.form['email'],request.form['query'],datetime.now(),"","")
      db.session.add(contactquery)
      db.session.commit()
      flash('Record was successfully added')
      return redirect(url_for('showall'))
   else:
      return render_template('contact.html')


# @app.route('/about')
# def about():
#    return render_template('about.html')

# @app.route('/logout')
# def logout():
#    session.pop('username', None)
#    return redirect(url_for('index'))


# @app.route('/output')
# def output():
#    return render_template('testResult.html', tempquery = tempquerys.query.all() )

# @app.route('/new', methods = ['GET', 'POST'])
# def new():
#    if request.method == 'POST':
#       if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#          flash('Please enter all the fields', 'error')
#       else:
#          student = students(request.form['name'], request.form['city'],
#             request.form['addr'], request.form['pin'])
         
#          db.session.add(student)
#          db.session.commit()
#          flash('Record was successfully added')
#          return redirect(url_for('output'))
#    return render_template('new.html')


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
   db.create_all()
   app.run(debug = True)