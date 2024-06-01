from database import db
class ProductInventorys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchasedate = db.Column('purchasedate',db.String(30))
    productname = db.Column('productname',db.String(30))
    productdescription = db.Column('productdescription',db.String(30))
    productcategory = db.Column('productcategory',db.String(30))
    productQuantity = db.Column('productQuantity',db.String(30))
    skunumber = db.Column('skunumber',db.String(30))
    productimage = db.Column('productimage',db.String(30))
    productprice = db.Column('productprice',db.String(30))
    margin = db.Column('margin',db.String(30))
    manufacturer = db.Column('manufacturer',db.String(30))
    seller = db.Column('seller',db.String(30))
    location = db.Column('location',db.String(30))

    def __init__(self, purchasedate, productname, productdescription, productcategory, productQuantity, skunumber, productimage, productprice,margin, manufacturer,seller,location):
        self.purchasedate = purchasedate
        self.productname = productname
        self.productdescription = productdescription
        self.productcategory = productcategory
        self.productQuantity = productQuantity
        self.skunumber = skunumber
        self.productimage = productimage
        self.productprice = productprice
        self.margin = margin
        self.manufacturer= manufacturer
        self.seller=seller
        self.location=location
    
    def to_dict(self):
        return {
            'id': self.id,
            'Purchase Date': self.purchasedate,
            'Product Name': self.productname,
            'Product Description': self.productdescription,
            'Product Category': self.productcategory,
            'Product Quantity': self.productQuantity,
            'SKU Number': self.skunumber,
            'Product Image': self.productimage,
            'Product Price': self.productprice,
            'Margin': self.margin,
            'Manufacturer': self.manufacturer,
            'Seller': self.seller,
            'Location': self.location
        }