from flask import Blueprint
from flask import render_template,session,redirect,url_for,request,json,flash 
from models.maidbooking import MaidBookings
from database import db

# Create a blueprint
my_maidProfile = Blueprint('my_maidProfile', __name__)

# Define other routes...
@my_maidProfile.route('/bookmaid', methods = ['GET', 'POST'])
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
    return render_template('maidprofile/bookingMaid.html')

@my_maidProfile.route('/maidsummary')
def maidsummary():
      return render_template('maidprofile/maidsummary.html',maidBookings = MaidBookings.query.all())   
