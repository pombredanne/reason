from reason import app, db
from reason.models import User, Report
from reason import views
from flask.ext.script import Manager, prompt_bool, Server
from flask.ext.migrate import Migrate, MigrateCommand 
import os, subprocess
from reason.vfeed.vfeedQuickUpdate import now as updatevFeed
import tempfile
import shutil
from contextlib import contextmanager


@contextmanager
def TemporaryDirectory():
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path, ignore_errors=True)


@contextmanager
def ChDir(new_dir):
    old_dir = os.getcwd()
    os.chdir(new_dir)
    yield
    os.chdir(old_dir)


manager= Manager(app)
#manager.add_command("runserver", Server(host="0.0.0.0", port=8095))
#migrate = Migrate(app, db)
#manager.add_command('db', MigrateCommand)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="sai", email="sai@email.com", password="sai"))
    db.session.commit()
    print("database initialized")


# Drop the database - Ooops!
##############################
### This is a danger zone! ###
##############################
@manager.command
def dropdb():
    if prompt_bool("Are you sure that you want to loose the data? Reports and users will be reset"):
	db.drop_all()
	print("Dropped Database")


# Update vulnerabilities database
@manager.command
def update():
    print("This feature is to be added - It will update databases")
    if prompt_bool("Updating database can take a while, Sip a Coffee?"):
	currentDir = os.getcwd()
	# Updates the original location with vfeed - For cli usage
    with ChDir('reason/vfeed'):
        updatevFeed()
    #Update Dependency-Check
    with TemporaryDirectory() as tempdir:
        args = [
            'reason/dependency-check/bin/dependency-check.sh',
            '--app', 'null',
            '--scan', '/dev/null',
            '--out', tempdir
            ]
        subprocess.call(args)

server = Server(host="0.0.0.0", port=8095)
manager.add_command("runserver", server)


if __name__ == '__main__':
    server = Server(host="0.0.0.0", port=8095)
    manager.run()
