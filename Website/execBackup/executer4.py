from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

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

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)