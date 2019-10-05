from service.userinfo import UserService
from model.model import db, Users, Products, Supplier_Master
from datetime import datetime
from sqlalchemy.sql import text


db.create_all()

class UserImplementation(UserService):

    def addUser(self,user):
        dbuser= self.getUser(user.email)
        #if dbuser:
        #    return
        print(user)
        db.session.add(user)
        db.session.commit()
        db.session.remove()

    def getUser(self,uemail):
        return Users.query.filter_by(email=uemail)

    def getAllUsers(self):
        return Users.query.all()

    def deleteUser(self,uid):
        dbUser = self.getUser(uid)
        if dbUser:
            db.session.delete(dbUser)
            db.session.commit()
            db.session.remove()
            return
        print('Record cannot be deleted')

    def updateUser(self,user):
        pass

    def getAllProducts(self):
        return Products.query.all()

    def getProductbyid(self, pid):
        print (pid)
        return Products.query.filter_by(product_id=pid).first()


    def getProductbyname(self, name):
        query = ('select * from products where product_name='+name)
        p = query
        return p

    def addProduct(self, nproduct):
        print(nproduct.product_name)
        dbp = self.getProductbyname(nproduct.product_name)
        # if dbp:
        #     return 'Product with same name already exist'
        db.session.add(nproduct)
        db.session.commit()
        db.session.remove()
        return 'Product Added Successfully'

    def updateProduct(self, product):
        print (product.product_id)
        dbp = self.getProductbyid(product.product_id)
        if dbp:
            dbp.product_name = product.product_name
            dbp.unit_type = product.unit_type
            dbp.product_description = product.product_description
            dbp.modified_by = product.modified_by
            # time = datetime.now().strftime("%B %d, %Y %I:%M%p")
            dbp.modified_on = datetime.now()
            db.session.commit()
            db.session.remove()
            return 'Product Updated Successfully'
        return 'Product Not Available to update'

    def deleteproduct(self,id):
        product = self.getProductbyid(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            db.session.remove()
            return 'Deleted Successfully'
        return 'Something went wrong, Product can not be deleted'

    def getAllSuppliers(self):
        return Supplier_Master.query.all()

    def getSupplierbyid(self,id):
        return Supplier_Master.query.filter_by(supplier_id=id).first()

    def addSupplier(self,supplier):
        db.session.add(supplier)
        db.session.commit()
        db.session.remove()
        return 'Supplier Added Successfully'

    def deleteSupplier(self,id):
        supplier = self.getSupplierbyid(id)
        if supplier:
            db.session.delete(supplier)
            db.session.commit()
            db.session.remove()
            return 'Deleted Successfully'
        return 'Something went wrong, Supplier can not be deleted'

    def updateSupplier(self,supplier):
        dbs = self.getSupplierbyid(supplier.supplier_id)
        if dbs:
            dbs.first_name = supplier.first_name
            dbs.last_name = supplier.last_name
            dbs.address = supplier.address
            dbs.village = supplier.village
            dbs.city = supplier.city
            dbs.state = supplier.state
            dbs.supplier_mobile = supplier.supplier_mobile
            dbs.modified_by = supplier.modified_by
            # time = datetime.now().strftime("%B %d, %Y %I:%M%p")
            dbs.modified_on = datetime.now()
            db.session.commit()
            db.session.remove()
            return 'Supplier Updated Successfully'
        return 'Supplier Not Available to update'