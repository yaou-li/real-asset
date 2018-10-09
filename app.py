from flask import Flask
from flaskext.mysql import MySQL
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from database import db
import config
import time
import json
import os
import sys

app = Flask('app')
mysql = MySQL()
app.config.from_object(config)

db.app = app
db.init_app(app)

mysql.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


from models.District import District
from models.Neighborhood import Neighborhood
from models.Vendor import Vendor

@manager.command
def create_db():
	db.create_all()
	db.session.commit()

@manager.command
def upgrade_db(sql):
    if not os.path.exists('migrations'):
        print ' ---------- init migrate ----------'
        os.system("python {} db init".format(sys.argv[0]))
    print ' ---------- migrate ----------'
    if os.system("python {} db migrate".format(sys.argv[0])):
        print 'failed to upgrade database'
    else:
        print ' ---------- upgrade ----------'
        db.session.execute('SET GLOBAL FOREIGN_KEY_CHECKS = 0')
        os.system("python {} db upgrade {}".format(sys.argv[0], '--sql' if sql else ''))
        db.session.execute('SET GLOBAL FOREIGN_KEY_CHECKS = 1')
