from peewee import *

spdxdb = PostgresqlDatabase('spdx', **{'password': 'spdx', 'user': 'spdx'})

class packages(Model):
    package_id = IntegerField(primary_key=True)
    name = TextField()
    version = TextField()
    comment = TextField()
    sha1 = TextField()

    class Meta:
        database = spdxdb


class files(Model):
    file_id = IntegerField(primary_key=True)
    
    class Meta:
        database = spdxdb

class packages_files(Model):
    package_id = ForeignKeyField(db_column='package_id', rel_model=packages, to_field='package_id')
    file_id = ForeignKeyField(db_column='file_id', rel_model=files, to_field='file_id')
    
    class Meta:
        database = spdxdb

class licenses(Model):
    license_id = IntegerField(primary_key=True)
    short_name = TextField()
    name = TextField()
    
    class Meta:
        database = spdxdb


class files_licenses(Model):
    file_id = ForeignKeyField(db_column='file_id', rel_model=files, to_field='file_id')
    license_id = ForeignKeyField(db_column='license_id', rel_model=licenses, to_field='license_id')
    
    class Meta:
        database = spdxdb


