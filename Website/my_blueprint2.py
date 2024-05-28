from flask import Blueprint,jsonify
from flask import render_template
from models.productInventory import ProductInventorys 

# Create a blueprint
my_blueprint2 = Blueprint('my_blueprint2', __name__)

@my_blueprint2.route('/curdoperator')
def curdoperator():
   return render_template('curdOperation.html')

@my_blueprint2.route('/intro')
def intro():
   products = ProductInventorys.query.all() 
   inventory_list=[{'id':product.id, 
                    'Purchase date':product.purchasedate}for product in products]
   return jsonify(inventory_list)