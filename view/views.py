from model.model import Users,app,db,Products,Supplier_Master
from flask import request,render_template, session
from implementation.userimpl import UserImplementation

SESSION_TYPE = 'filesystem'
uimpl = UserImplementation()
userr = ''

@app.route('/index/', methods=['POST','GET'])
def index():
    scount = 0
    tp = uimpl.getAllSuppliers()
    for i in tp:
        scount += 1
    print (scount)
    return render_template('index.html', sc=scount, user=session['username'])

@app.route('/signup/', methods=['POST'])
def userreg():
    blankuser = Users(user_id=0,first_name='',last_name='',email='',password='',is_admin=True)
    if request.method =='POST':
        user_id = 1
        tu = uimpl.getAllUsers()
        for i in tu:
            user_id+=1
        first_name = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        is_admin = True
        if password != cpassword:
            rmsg = 'Password & Confirm Password must be same'
        else:
            newuser=Users(user_id=user_id,first_name=first_name,last_name=lastname,email=email,password=password,is_admin=is_admin)
            uimpl.addUser(newuser)
            rmsg = 'User Added Successfully. You can Login Now :)'
        return render_template('login_main.html',msg=rmsg)
    return render_template('login_main.html', msg='signup get')

@app.route('/login_main/', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'POST':
        username = request.form['uid']
        userpass = request.form['password']
        user = Users.query.filter_by(email=username).first()

        if user:
            if user.password == userpass:
                print("Login Successful")
                un = user.first_name + ' ' + user.last_name
                session['username'] = un
                session['suid'] = user.user_id
                return render_template('index.html', user=session['username'])
            return render_template('login_main.html', msg='Please enter a valid Password')
        return render_template('login_main.html', msg='Invalid User Name')
        # if username !=''or userpass !='':
        #     user = Users.query.filter_by(email=username).first()
        #     if user.email == username and user.password == userpass:
        #         print("Login Successful")
        #         un = user.first_name+' '+user.last_name
        #         # Session['username'] = un
        #         return render_template('index.html', user=un)
    return  render_template('login_main.html', msg='Get ')

@app.route('/')
def home():
    return render_template('login_main.html', msg='')

@app.route('/logout')
def sessionlogout():
    session.pop('username', None)
    return render_template('login_main.html', msg='')

@app.route('/products/', methods=['GET','POST'])
def product():
    emptp = Products(product_id='', product_name='', unit_type='', product_description='')
    if request.method == 'POST':
        if request.form['pid'] == 0 or request.form['pid'] == '':
            product_id = 1
            tp = uimpl.getAllProducts()
            for i in tp:
                product_id += 1
            newproduct = Products(product_id=product_id , product_name=request.form['pname'], unit_type=request.form['uom'] ,
                                  product_description=request.form['pdesc'], created_by=session['suid'], modified_by=session['suid'])
            rmsg = uimpl.addProduct(newproduct)
            listofp = uimpl.getAllProducts()
            return render_template('products.html', msg=rmsg, emptp=emptp, plist=listofp, user=session['username'])
        else:
            product_id = request.form['pid']
            newproduct = Products(product_id=product_id, product_name=request.form['pname'],
                                  unit_type=request.form['uom'],
                                  product_description=request.form['pdesc'],modified_by=session['suid'])
            rmsg = uimpl.updateProduct(newproduct)
            listofp = uimpl.getAllProducts()
            return render_template('products.html', msg=rmsg, user=session['username'], emptp=emptp, plist=listofp)
    rmsg = ''
    listofp = uimpl.getAllProducts()
    return render_template('products.html', msg=rmsg, user=session['username'], plist=listofp, emptp=emptp)

@app.route('/productdelete/<id>', methods=['GET'])
def deleteproduct(id):
    emptp = Products(product_id='', product_name='', unit_type='', product_description='')
    rmsg = uimpl.deleteproduct(id)
    listofp = uimpl.getAllProducts()
    return render_template('products.html', msg=rmsg, emptp=emptp, plist=listofp, user=session['username'])

@app.route('/productedit/<id>', methods=['GET'])
def editproduct(id):
    ptoedit = uimpl.getProductbyid(id)
    listofp = uimpl.getAllProducts()
    print(ptoedit)
    return render_template('products.html', msg='', emptp=ptoedit, plist=listofp, user=session['username'])

@app.route('/suppliermaster/', methods=['GET','POST'])
def supplier():
    emptys = Supplier_Master(supplier_id='', first_name='', last_name='', address='', village='', city='', state='',
                             supplier_mobile='', supplier_mobile2='')
    if request.method == 'POST':
        if request.form['sid'] == 0 or request.form['sid'] == '':
            supplier_id = 1
            tp = uimpl.getAllSuppliers()
            for i in tp:
                supplier_id += 1
            newsupplier = Supplier_Master(supplier_id=supplier_id, first_name=request.form['fname'],
                                  last_name=request.form['lname'], address=request.form['address'],
                                    village=request.form['village'], city=request.form['city'],
                                    state=request.form['state'], supplier_mobile=request.form['mobile'],
                                  supplier_mobile2='', created_by=session['suid']
                                          , modified_by=session['suid'])
            rmsg = uimpl.addSupplier(newsupplier)
            listofs = uimpl.getAllSuppliers()
            return render_template('suppliermaster.html', msg=rmsg, emptys=emptys, slist=listofs, user=session['username'])
        else:
            supplier_id = request.form['sid']
            newsupplier = Supplier_Master(supplier_id=supplier_id, first_name=request.form['fname'],
                                  last_name=request.form['lname'], address=request.form['address'],
                                    village=request.form['village'], city=request.form['city'],
                                    state=request.form['state'], supplier_mobile=request.form['mobile'],
                                  supplier_mobile2='', modified_by=session['suid'])
            rmsg = uimpl.updateSupplier(newsupplier)
            listofs = uimpl.getAllSuppliers()
            return render_template('suppliermaster.html', msg=rmsg, user=session['username'], emptys=emptys, slist=listofs)
    rmsg = ''
    listofs = uimpl.getAllSuppliers()
    return render_template('suppliermaster.html', msg=rmsg, user=session['username'], slist=listofs, emptys=emptys)


@app.route('/supplierdelete/<id>', methods=['GET'])
def deletesupplir(id):
    emptys = Supplier_Master(supplier_id='', first_name='', last_name='', address='', village='', city='', state='',
                             supplier_mobile='', supplier_mobile2='')
    rmsg = uimpl.deleteSupplier(id)
    listofs = uimpl.getAllSuppliers()
    return render_template('suppliermaster.html', msg=rmsg, emptys=emptys, slist=listofs, user=session['username'])

@app.route('/supplieredit/<id>', methods=['GET'])
def editsupplier(id):
    stoedit = uimpl.getSupplierbyid(id)
    listofs = uimpl.getAllSuppliers()
    print(stoedit)
    return render_template('suppliermaster.html', msg='', emptys=stoedit, slist=listofs, user=session['username'])

@app.route('/purchase/', methods=['GET'])
def purchase():
    suppliers = uimpl.getAllSuppliers()
    listofp = uimpl.getAllProducts()
    return render_template('purchase.html', msg='', suppliers=suppliers, products=listofp, user=session['username'])

#from flask import request, jsonify
'''
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]
# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)
    
ptoedit = uimpl.getProductbyid(id)
listofp = uimpl.getAllProducts()
dir = {}
dir["PRD_ID"] = ptoedit
dir["PRDS"] = listofp

li = [ptoedit, listofp]
return jsonify(li)
'''


if __name__=='__main__':
    app.run(port=5051,debug=True)