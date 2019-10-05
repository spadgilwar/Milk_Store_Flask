from abc import ABC,abstractmethod

class UserService(ABC):

    @abstractmethod
    def addUser(self,user):
        pass

    def getUser(self,uid):
        pass
    def getAllUsers(self):
        pass
    def deleteUser(self,uid):
        pass
    def updateUser(self,user):
        pass
    def getAllProducts(self):
        pass
    def getProductbyname(self,name):
        pass
    def getProductbyid(self,id):
        pass
    def addProduct(self,product):
        pass
    def updateProduct(self,product):
        pass
    def deleteproduct(self,id):
        pass
    def getAllSuppliers(self):
        pass
    def getSupplierbyid(self,id):
        pass
    def addSupplier(self,supplier):
        pass
    def updateSupplier(self,supplier):
        pass
    def deleteSupplier(self,id):
        pass