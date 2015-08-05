from peewee import * 
from playhouse.sqlite_ext import *
from playhouse.sqlite_ext import SqliteDatabase
from vfeedModel import nvd_db, cve_cpe, cve_cwe
from vfeedModel import map_cve_exploitdb
import os


basedir = os.path.abspath(os.path.dirname(__file__))
database = os.path.join(basedir, 'db/report.db')

db = SqliteDatabase(database)

class Notify(Model):
    rec_id = IntegerField(primary_key=True, unique=True)
    cpes_for_pkg = TextField()
    cves_for_pkg = TextField()
    cwes_for_pkg = TextField()
    exp_for_pkg = TextField()

    class Meta:
        database=db

# To uncomment when this is ready for spdxDB
'''
class Reports(Model):
    report_id = IntegerField(primary_key=True, unique=True)
    pkg_id = IntegerField()
    lic_short_name = TextField()
    cpes_for_pkg = ForeignKeyField(db_column='cpes_for_pkg', rel_model=Notify, to_field='cpes_for_pkg')
    cves_for_pkg = ForeignKeyField(db_column='cves_for_pkg', rel_model=Notify, to_field='cves_for_pkg')
    cwes_for_pkg = ForeignKeyField(db_column='cwes_for_pkg', rel_model=Notify, to_field='cwes_for_pkg')
    exp_for_pkg = ForeignKeyField(db_column='exp_for_pkg', rel_model=Notify, to_field='exp_for_pkg')
 
    class Meta:
        database=db
'''

class FTS_reportsModel(FTSModel):
    
    
    class Meta:
        database=db
