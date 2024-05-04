#model/maidBooking
from database import db

class MaidBookings(db.Model):
    id = db.Column('bookingID',db.Integer, primary_key=True)
    bookingdate = db.Column('bookingDate',db.String(20))
    timeslot = db.Column('timeslot',db.String(10))
    category = db.Column('category',db.String(30))
    customername = db.Column('customername',db.String(30))
    housenumber = db.Column('housenumber',db.String(20))
    address1=db.Column('address1',db.String(20))
    address2=db.Column('address2',db.String(20))
    state=  db.Column('state',db.String(20))
    district=db.Column('district',db.String(20))    

    def __init__(self,bookingdate,timeslot,category,customername,housenumber,address1,address2,state,district):
        self.bookingdate =bookingdate
        self.timeslot   = timeslot
        self.category =category
        self.customername=customername
        self.housenumber=housenumber
        self.address1= address1
        self.address2= address2
        self.state= state
        self.district=district

