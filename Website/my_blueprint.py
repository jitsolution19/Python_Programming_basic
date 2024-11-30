from flask import Blueprint
from flask import render_template,session,redirect,url_for 

# Create a blueprint
my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/about')
def about():
   return render_template('aboutUs/AboutUs.html')

@my_blueprint.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

@my_blueprint.route('/register')
def register():
    return render_template('register.html')

@my_blueprint.route('/SignIn')
def sign_in():
    if session.get('logged_in'):
        return render_template('signIn.html', message=session['username'])
    else:
        return render_template('index.html')
