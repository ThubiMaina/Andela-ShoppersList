from flask import Flask,render_template,request,flash
from user import User
from flask import session
import os




app = Flask(__name__)
app.secret_key = os.urandom(24)
newUser = User()

@app.route('/')

def index():
    return render_template("home.html")

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = newUser.login(email, password)
        print(result)
    return render_template("login.html") 

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        print(username, email, password, cpassword,">>>")
        result = newUser.register(email, username, password, cpassword)

        if result == 1:
            session['user'] = username
            message = "Account created sucessfully"
            return render_template('home.html', data = message)

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

@app.route('/create')
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
    return render_template("Create.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")        



if __name__ == "__main__":
    app.run(debug=True)