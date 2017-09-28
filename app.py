from flask import Flask,render_template,request,session,redirect,url_for
from user import User
from shopperlist import ShopperList
import os




app = Flask(__name__)
app.secret_key = os.urandom(24)
newUser = User()
shoplist = ShopperList()

@app.route('/')

def index():
    return render_template("home.html")

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = newUser.login(email, password)
        if result == 1:
            username = newUser.get_user_name(email)
            email = newUser.get_user_email(email)
            session['user'] = username
            session['email'] = email
            return render_template('home.html', data=session)
        elif result == 2:
            error = "Password mismatch"
            return render_template('login.html', data=error)	
        elif result == 3:
            error = "The user does not exist please register and try again"
            return render_template('login.html', data=error)	
        elif result == 4:
            error = "Please fill all the fields"
            return render_template('login.html', data=error)	 	
        else:
            error = "Wrong credentials please try again"
            return render_template ('login.html',data=error) 
    else:
        return render_template('login.html') 

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        result = newUser.register(email, username, password, cpassword)

        if result == 1:
            session['user'] = username
            message = "Account created sucessfully"
            return render_template('login.html', data = message)

        elif result == 6:
            message = ("please fill all the fields")
            return render_template('signup.html', data = message)
        elif result == 8:
            message = ("Special characters not allowed in field name")
            return render_template('signup.html', data=message)
        elif result == 7:
            message = (
                "Password should have minimum six characters, at least one letter and one number")
            return render_template('signup.html', data=message)
        elif result == 5:
            message = ("User name has alredy been taken")
            return render_template('signup.html', data=message)
        elif result == 3:
            message = ("password do not match")
            return render_template('signup.html', data=message)
        elif result == 2:
            error = "email must be a valid email"
            return render_template('signup.html', data=error)
        elif result == 4:
            error = "email already registered"
            return render_template('signup.html', data=error)
    return render_template('signup.html')
        
    return render_template("signup.html")

@app.route('/create' ,methods = ['POST','GET'])
def create():
    
    if  'email' in session:
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            result = shoplist.create(name ,description)
            
        return render_template("Create.html")
    error = 'you have to be logged in'
    return render_template('login.html')


@app.route('/create' ,methods = ['GET'])
def getshoppinglists():
    if request.method == 'GET':
        result = shoplist.get_shoppinglist()
        if (result != {}):
            return render_template('dashboard.html', data=result)
        else:
            error = "create a shopping list first"
            return render_template('Create.html', data=error)
        
    return render_template("Create.html")

@app.route('/dashboard')
def dashboard():
    if request.method == 'GET':
        result = shoplist.get_shoppinglist()
    
        return render_template('dashboard.html', data=result)
        

@app.route('/logout')
def logout():
    """Handles requests to logout a user"""
    session.pop('email', None)
    error = 'You are logged out'
    return redirect(url_for('index') )

if __name__ == "__main__":
    app.run(debug=True)