import os
from user import User
from shoppinglists import Shoppinglist
from flask import session, render_template, request, redirect, g, url_for
from app import app

newUser = User()

app.secret_key = os.urandom(24)

@app.route('/signup', methods=['GET', 'POST'])
def register():
    """Handles the requests for the register view"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        print(username, email, password, cpassword)
        result = newuser.register(email, username, password, cpassword)
        if result == 1:
            session['user'] = username
            message = "Account created sucessfully"
            return render_template('home.html', data=message)

        elif result == 6:
            message = ("please fill all the fields")
            return render_template('signup.html', data=message)
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