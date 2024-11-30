from flask import Blueprint,jsonify,request,flash
from flask import render_template
from models.productInventory import ProductInventorys 
from database import db
from sqlalchemy import text

# Create a blueprint
my_blueprint2 = Blueprint('my_blueprint2', __name__)

@my_blueprint2.route('/curdoperator')
def curdoperator():
   return render_template('curdOperation.html')

@my_blueprint2.route('/intro')
def intro():
   products = ProductInventorys.query.all() 
   # inventory_list=[{'id':product.id, 
   #                  'Purchase date':product.purchasedate}for product in products]
   inventory_list = [product.to_dict() for product in products]
   return jsonify(inventory_list)

@my_blueprint2.route('/addOperation', methods = ['GET', 'POST'])
def addOperation():
   if request.method == 'POST':
      if request.is_json:
          data = request.get_json()
          purchase_date = data.get("Purchase Date")
          flash(purchase_date)
         #  db.session.execute(
         #       text("INSERT INTO ProductInventorys (purchasedate) VALUES (:purchase_date)"),
         #        {"purchase_date": purchase_date}
         #  )
          new_product = ProductInventorys(purchasedate=purchase_date,
                                          productname="",
                                          productdescription="",
                                          productcategory="",
                                          productQuantity="",
                                          skunumber="",
                                          productimage="",
                                          productprice="",
                                          margin="",
                                          manufacturer="",
                                          seller="",
                                          location=""                                          
                                       )
          db.session.add(new_product)
          db.session.commit()         
      else:
         return "Request was not JSON", 400
      return ('Added data succesfully in database')
   else:
      return ('Unable to Add the data in database. Please try again')

   #  if request.method == 'POST':
   #          inventoryaddition = ProductInventorys(request.form['purchasedate'],request.form['productname'],request.form['productdescription'],request.form['productcategory'],request.form['productQuantity'],request.form['skunumber'],request.form['productimage'],request.form['productprice'],request.form['margin'],request.form['manufacturer'],request.form['seller'],request.form['location'])
   #          db.session.add(inventoryaddition)
   #          db.session.commit()
   #          flash('Record was successfully added')
   #          return redirect(url_for('inventory'))
   # else:            
   # return render_template('product.html', guest=session['username'])

@my_blueprint2.route('/deleteInventory',  methods = ['GET', 'POST'])
def deleteInventory():
   if request.method == 'POST':
      if request.is_json:
          data = request.get_json()
          productID = data.get("ID")
          flash(productID)
          product = ProductInventorys.query.filter_by(id=productID).first()
          if product:
             db.session.delete(product)   
             db.session.commit()          
             return jsonify(f"Product with ID {productID} deleted successfully.")
          else:
             return jsonify(f"Product with ID {productID} not found."), 404
      else:
         return "Request was not JSON", 400
   else:
      return ('Unable to delete the data in database. Please try again')

@my_blueprint2.route('/updateInventory',  methods = ['GET', 'POST'])
def updateInventory():
   if request.method == 'POST':
      if request.is_json:
          data = request.get_json()
          productID = data.get("ID")
          sellerinfo = data.get("Seller")
          flash(productID)
          product = ProductInventorys.query.filter_by(id=productID).first()
          if product:
             product.seller =sellerinfo
             db.session.commit()          
             return jsonify(f"Seller info {sellerinfo} of Product with ID {productID} updated successfully.")
          else:
             return jsonify(f"Seller info {sellerinfo} of Product with ID {productID} not updated."), 404
      else:
         return "Request was not JSON", 400
   else:
      return ('Unable to update the data in database. Please try again'),405
