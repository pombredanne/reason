from flask import render_template, url_for, request, flash, send_file, make_response, redirect
from logging import DEBUG
from werkzeug import secure_filename
from formgen import pomxmlForm, LoginForm, SignupForm, searchForm
from reason import app, db, login_manager
from reason import ALLOWED_EXTENSIONS
from reason import basedir
from models import User, Report
from flask_login import login_required, login_user, logout_user, current_user
from validfile import validateFile
from vfeedWarp import search as searchfor
from callsocs import callsocs

from contextlib import contextmanager
import tempfile
import os
import shutil

@contextmanager
def TemporaryDirectory():
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path, ignore_errors=True)


###############################
### Custom Functions go here###
###############################

#Allowed filename check - Only extention is checked
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Login manage & load
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

######################
### Views go below ###
######################

# Index page Routing
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html', dependencyTitle="Reason", dependencyText="Software License and Security articat")

#Upload page route and Upload Definition
@login_required
@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = pomxmlForm()
    if form.validate_on_submit():
        filename = secure_filename(form.pomxml.data.filename)
        with TemporaryDirectory() as tempdir:
            saveAs = os.path.abspath(os.path.join(tempdir, filename))
            form.pomxml.data.save(saveAs)
            filesign = validateFile(saveAs)
            if filesign == "Good":
                results = callsocs(tempdir, saveAs)
                return render_template('data.html', results=results)
            else:
                flash('Invalid file')
	
    return render_template('upload.html', form=form)


# User Authentication and validation - Access to views and resources
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
	        login_user(user, form.remember_me.data)
	        return redirect(request.args.get('next') or url_for('user', username=user.username))
	else:
	    flash("Generous Monkey banging QWERTY! OR maybe a bruteforce attempt!")
    return render_template("login.html", form = form)

# User logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Per user route
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

#Search Page route
@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = searchForm()
    if form.validate_on_submit():
    	text = form.searchCont.data
        actionVal = form.actions.data
        return render_template('search.html', form=form, searchresults=searchfor(text, actionVal))
    
    else:
	    flash("Search format => cpe:/a:apache:http_server:0.8.14 or CVE-2011-1234")
	    flash("Free text search => Upcoming!")
    
    return render_template('search.html', form=form)


# Sign-Up page
@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
	user = User(email=form.email.data, username=form.username.data, password = form.password.data)
	
        db.session.add(user)
        db.session.commit()
        flash('Welcome, {}! Please login.'.format(user.username))
	return redirect(url_for('login'))
    else:
	flash("Contact admin if there are problems with sign-up")
	
    return render_template('signup.html', form=form)

    
#404 Response
@app.errorhandler(404)
@login_required
def page_not_found(e):
    return render_template('404.html'), 404

#Server side error response
@app.errorhandler(500)
@login_required
def page_not_found(e):
    return render_template('500.html'), 500

