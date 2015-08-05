import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import datetime
from flask.ext.moment import Moment
from flask_debugtoolbar import DebugToolbarExtension


basedir = os.path.abspath(os.path.dirname(__file__))
app =  Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(60)

userDb = 'sqlite:///' + os.path.join(basedir, 'db/reasonUser.db')
spdxDb = 'postgresql://spdx:spdx@host:5432/spdx'

# Initial URI was for searching from NVD Database, Made changes to connect to Users db using binds
# App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'nvd.vulnerabilities.db')

databases = {
    'userDb': userDb,    
}



app.config['SQLALCHEMY_BINDS'] = databases
# Debug configuration
app.config['DEBUG'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)
# Debug Configuration
#DEBUG_TB_INTERCEPT_REDIRECTS = False
#toolbar = DebugToolbarExtension(app)

ALLOWED_EXTENSIONS = set(['xml', 'jar'])
moment = Moment(app)


