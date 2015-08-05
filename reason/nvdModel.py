from peewee import *

database = SqliteDatabase('nvdparser/nvd.vulnerabilities.db', **{})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Cpe(BaseModel):
    cpe = PrimaryKeyField(db_column='cpe_id', null=True)
    cpe_text = TextField(null=True)
    edition = TextField(null=True)
    language = TextField(null=True)
    part = TextField(null=True)
    product = TextField(null=True)
    update_date = TextField(null=True)
    vendor = TextField(null=True)
    version = TextField(null=True)

    class Meta:
        db_table = 'cpe'

class DownloadDates(BaseModel):
    dldate = PrimaryKeyField(db_column='dldate_id', null=True)
    download_link = TextField(null=True)
    feed_size = FloatField(null=True)
    feed_year = TextField(null=True)
    last_download = IntegerField(null=True)

    class Meta:
        db_table = 'download_dates'

class Vulnerabilities(BaseModel):
    cve = TextField(index=True, null=True)
    cvss_score = FloatField(null=True)
    cwe = TextField(null=True)
    dldate = ForeignKeyField(db_column='dldate_id', null=True, rel_model=DownloadDates, to_field='dldate')
    modified_date = IntegerField(null=True)
    published_date = IntegerField(null=True)
    summary = TextField(null=True)
    vuln = PrimaryKeyField(db_column='vuln_id', null=True)

    class Meta:
        db_table = 'vulnerabilities'

class AffectsToCpe(BaseModel):
    affects_to_cpe = PrimaryKeyField(db_column='affects_to_cpe_id', null=True)
    cpe = ForeignKeyField(db_column='cpe_id', null=True, rel_model=Cpe, to_field='cpe')
    vuln = ForeignKeyField(db_column='vuln_id', null=True, rel_model=Vulnerabilities, to_field='vuln')

    class Meta:
        db_table = 'affects_to_cpe'

class SqliteSequence(BaseModel):
    name = UnknownField(null=True)  # 
    seq = UnknownField(null=True)  # 

    class Meta:
        db_table = 'sqlite_sequence'

