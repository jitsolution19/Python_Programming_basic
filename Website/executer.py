from flask import Flask,render_template,redirect,url_for,request,flash,session
app = Flask(__name__)
app.secret_key="Shivansh2021"

@app.route('/')
def index():
   return render_template('index.html') 

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route('/SignIn')
def signIn():
   username = session['username']
   return render_template('signIn.html',message = username)

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
   # user = session['username']
   if session.get('logged_in')==True:
      return render_template('product.html', guest = session['username'])
   else:
      return redirect(url_for('index') )                          




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