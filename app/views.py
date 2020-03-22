# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session
from flask_login import login_user, logout_user, current_user, login_required
from app import app, lm, db
from forms import ExampleForm, LoginForm, NewAccountForm
from models import User

@app.route('/')
def index():
	if g.user is not None and g.user.is_authenticated():
		user_loggedIn = True
	return render_template('index.html')


@app.route('/list/')
def posts():
	return render_template('list.html')

@app.route('/new/')
@login_required
def new():
	form = ExampleForm()
	return render_template('new.html', form=form)

@app.route('/save/', methods = ['GET','POST'])
@login_required
def save():
	form = ExampleForm()
	if form.validate_on_submit():
		print "salvando os dados:"
		print form.title.data
		print form.content.data
		print form.date.data
		flash('Dados salvos!')
	return render_template('new.html', form=form)

@app.route('/view/<id>/')
def view(id):
	return render_template('view.html')

# === User login methods ===

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=g.id).first()

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        login_user(g.user)
        print("User " + str(g) + " logged in.")
        return redirect(url_for('index'))

    return render_template('login.html', 
        title = 'Sign In',
        form = form)

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/newacc/', methods = ['GET', 'POST'])
def newacc():

    form = NewAccountForm()
    if form.validate_on_submit():
    	print(form.user.data)
    	print(form.email.data)
    	db.create_all()
     	new_user = User(user=form.user.data, email=form.email.data, password=form.password.data)
     	db.session.add(new_user)
     	db.session.commit()
     	return redirect(url_for('index'))

    return render_template('newacc.html', 
        title = 'Create new account',
        form = form)

    # ===================
