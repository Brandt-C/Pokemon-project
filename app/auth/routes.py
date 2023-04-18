from flask import Blueprint, render_template, request, url_for, redirect, flash
from .forms import SignUpForm, LoginForm
from app.models import User, db, current_user
from flask_login import logout_user, login_user, current_user
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')
from flask_login import logout_user

@auth.route('/test')
def login():
    return render_template('test.html')


@auth.route('/register', methods=['GET', 'POST'])
def registerPage():
    form = SignUpForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)

            user = User(username, email, password)
            user.saveUser()

            flash(f'Welcome to Battle Pokemon {user,username}', 'success')
            return redirect(url_for('auth.loginPage'))

    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def loginPage():
    form = LoginForm()
    print(request.method)
    if request.method == 'POST':
        print(request.method)
        if form.validate():
            username = form.username.data
            password = form.password.data

        user = User.query.filter_by(username=username).first()
            #   SELECT * FROM user WHERE username = <username variable>
        if user:
            if check_password_hash(user.password, password): # <-- NEW
                # user.password == password: -- OLD way
                print("YAY, you're logged in!")
                login_user(user)
                print(current_user)
                print(current_user.username)
                return redirect(url_for('homePage'))
            else:
                flash("Incorrect Password!", "warning")
        else:
            flash("Username is Incorrect!", "danger")
        return redirect(url_for('auth.loginPage'))
    return render_template('login.html', form=form)
        

@auth.route('/logout')
def logout():
      logout_user()
      return redirect(url_for('homePage'))

