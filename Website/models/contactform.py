#model/contacts
from database import db

# Define Contact Query Model
class ContactQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name',db.String(30))
    mobilenumber = db.Column('mobilenumber',db.Integer)
    email = db.Column('email',db.String(20))
    querytext = db.Column('querytext',db.String(150))
    creationdate = db.Column('creationdate',db.String(30))
    status = db.Column('status',db.String(30))
    closingdate = db.Column('closingdate',db.String(30))

    def __init__(self, name, mobilenumber, email, querytext, current_date, status, closingdate):
        self.name = name
        self.mobilenumber = mobilenumber
        self.email = email
        self.querytext = querytext
        self.creationdate = current_date
        self.status = status
        self.closingdate = closingdate
