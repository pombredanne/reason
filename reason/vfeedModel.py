from peewee import *
from playhouse.sqlite_ext import *
from playhouse.sqlite_ext import SqliteExtDatabase
import os

basedir = os.path.abspath(os.path.dirname(__file__))
database = os.path.join(basedir,'vfeed/vfeed.db')
db = SqliteDatabase(database)


class nvd_db(Model):
    cveid = TextField(primary_key=True)
    date_published =DateField()
    date_modified = DateField()
    summary = TextField()
    cvss_base = TextField()
    cvss_impact = TextField()
    cvss_exploit = TextField()
    cvss_access_vector = TextField()
    cvss_access_complexity = TextField()
    cvss_authentication = TextField()
    cvss_confidentiality_impact = TextField()
    cvss_integrity_impact = TextField()
    cvss_availability_impact = TextField()


class cve_cpe(Model):
    cpeid = TextField(primary_key=True)
    cveid = ForeignKeyField(db_column='cveid', rel_model=nvd_db, to_field='cveid')

    class Meta:
        database=db

class cve_cwe(Model):
    cveid = ForeignKeyField(db_column='cveid', rel_model=nvd_db, to_field='cveid')
    cweid = TextField()

    class Meta:
        database = db

class map_cve_exploitdb(Model):
    exploitdbid = TextField()
    exploitdbscript = TextField()
    cveid = ForeignKeyField(db_column='cveid', rel_model=nvd_db, to_field='cveid')
    
    class Meta:
        database=db



class FTS_CVE(FTSModel):
    cpeid=ForeignKeyField(cve_cpe)
    cveid=TextField()
    cweid=TextField()
    exploitdbid = TextField()
    
    class Meta:
        database=db


