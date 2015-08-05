from peewee import *

spdxdb = PostgresqlDatabase('spdx', **{'password': 'spdx', 'user': 'spdx'})


class annotation_types(Model):
    annotation_type = PrimaryKeyField(db_column='annotation_type_id')
    name = CharField(unique=True)

    class Meta:
        database = spdxdb

class document_namespaces(Model):
    document_namespace = PrimaryKeyField(db_column='document_namespace_id')
    uri = CharField(unique=True)

    class Meta:
        database = spdxdb

class licenses(Model):
    comment = TextField()
    cross_reference = TextField()
    is_spdx_official = BooleanField()
    license = PrimaryKeyField(db_column='license_id')
    name = CharField(null=True)
    short_name = CharField(unique=True)

    class Meta:
        database = spdxdb

class creator_types(Model):
    creator_type = PrimaryKeyField(db_column='creator_type_id')
    name = CharField()

    class Meta:
        database = spdxdb

class creators(Model):
    creator = PrimaryKeyField(db_column='creator_id')
    creator_type = ForeignKeyField(db_column='creator_type_id', rel_model=creator_types, to_field='creator_type')
    email = CharField()
    name = CharField()

    class Meta:
        database = spdxdb

class projects(Model):
    homepage = TextField()
    name = TextField()
    project = PrimaryKeyField(db_column='project_id')
    uri = TextField()

    class Meta:
        database = spdxdb

class file_types(Model):
    file_type = PrimaryKeyField(db_column='file_type_id')
    name = CharField(unique=True)

    class Meta:
        database = spdxdb

class files(Model):
    comment = TextField()
    copyright_text = TextField(null=True)
    file_id = PrimaryKeyField(db_column='file_id')
    file_type = ForeignKeyField(db_column='file_type_id', rel_model=file_types, to_field='file_type')
    notice = TextField()
    project = ForeignKeyField(db_column='project_id', null=True, rel_model=projects, to_field='project')
    sha1 = CharField(unique=True)

    class Meta:
        database = spdxdb

class packages(Model):
    package_id = IntegerField(primary_key=True)

    class Meta:
        database = spdxdb

# Possible reference cycle: packages
class packages_files(Model):
    concluded_license = ForeignKeyField(db_column='concluded_license_id', null=True, rel_model=licenses, to_field='license')
    file_id = ForeignKeyField(db_column='file_id', rel_model=files, to_field='file')
    file_name = TextField()
    license_comment = TextField()
    package_file = PrimaryKeyField(db_column='package_file_id')
    package = ForeignKeyField(db_column='package_id', rel_model=packages, to_field='package_id')

    class Meta:
        database = spdxdb



class documents(Model):
    created_ts = DateTimeField()
    creator_comment = TextField()
    data_license = ForeignKeyField(db_column='data_license_id', rel_model=licenses, to_field='license')
    document_comment = TextField()
    document = PrimaryKeyField(db_column='document_id')
    document_namespace = ForeignKeyField(db_column='document_namespace_id', rel_model=document_namespaces, to_field='document_namespace', unique=True)
    license_list_version = CharField()
    name = CharField()
    package = ForeignKeyField(db_column='package_id', rel_model=packages, to_field='package')
    spdx_version = CharField()

    class Meta:
        database = spdxdb

class identifiers(Model):
    document = ForeignKeyField(db_column='document_id', null=True, rel_model=documents, to_field='document')
    document_namespace = ForeignKeyField(db_column='document_namespace_id', rel_model=document_namespaces, to_field='document_namespace')
    id_string = CharField()
    identifier = PrimaryKeyField(db_column='identifier_id')
    package_file = ForeignKeyField(db_column='package_file_id', null=True, rel_model=PackagesFiles, to_field='package_file')
    package = ForeignKeyField(db_column='package_id', null=True, rel_model=packages, to_field='package')

    class Meta:
        database = spdxdb

class annotations(BaseModel):
    annotation = PrimaryKeyField(db_column='annotation_id')
    annotation_type = ForeignKeyField(db_column='annotation_type_id', rel_model=annotation_types, to_field='annotation_type')
    comment = TextField()
    created_ts = DateTimeField(null=True)
    creator = ForeignKeyField(db_column='creator_id', rel_model=creators, to_field='creator')
    document = ForeignKeyField(db_column='document_id', rel_model=documents, to_field='document')
    identifier = ForeignKeyField(db_column='identifier_id', rel_model=identifiers, to_field='identifier')

    class Meta:
        database = spdxdb

class documents_creators(Model):
    creator = ForeignKeyField(db_column='creator_id', rel_model=creators, to_field='creator')
    document_creator = PrimaryKeyField(db_column='document_creator_id')
    document = ForeignKeyField(db_column='document_id', rel_model=documents, to_field='document')

    class Meta:
        database = spdxdb

class external_refs(Model):
    document = ForeignKeyField(db_column='document_id', rel_model=documents, to_field='document')
    document_namespace = ForeignKeyField(db_column='document_namespace_id', rel_model=document_namespaces, to_field='document_namespace')
    external_ref = PrimaryKeyField(db_column='external_ref_id')
    id_string = CharField()
    sha1 = CharField()

    class Meta:
        database = spdxdb

class file_contributors(Model):
    contributor = TextField()
    file_contributor = PrimaryKeyField(db_column='file_contributor_id')
    file = ForeignKeyField(db_column='file_id', rel_model=files, to_field='file')

    class Meta:
        database = spdxdb

class files_licenses(Model):
    extracted_text = TextField()
    file = ForeignKeyField(db_column='file_id', rel_model=files, to_field='file')
    file_license = PrimaryKeyField(db_column='file_license_id')
    license = ForeignKeyField(db_column='license_id', rel_model=licenses, to_field='license')

    class Meta:
        database = spdxdb

class scanners(Model):
    name = CharField(unique=True)
    scanner = PrimaryKeyField(db_column='scanner_id')

    class Meta:
        database = spdxdb

class files_scans(Model):
    file = ForeignKeyField(db_column='file_id', rel_model=files, to_field='file')
    file_scan = PrimaryKeyField(db_column='file_scan_id')
    scanner = ForeignKeyField(db_column='scanner_id', rel_model=scanners, to_field='scanner')

    class Meta:
        db_table = 'files_scans'

class packages_scans(Model):
    package = ForeignKeyField(db_column='package_id', rel_model=Packages, to_field='package')
    package_scan = PrimaryKeyField(db_column='package_scan_id')
    scanner = ForeignKeyField(db_column='scanner_id', rel_model=scanners, to_field='scanner')

    class Meta:
        database = spdxdb

class relationship_types(Model):
    name = CharField(unique=True)
    relationship_type = PrimaryKeyField(db_column='relationship_type_id')

    class Meta:
        database = spdxdb

class relationships(Model):
    left_identifier = ForeignKeyField(db_column='left_identifier_id', rel_model=Identifiers, to_field='identifier')
    relationship_comment = TextField()
    relationship = PrimaryKeyField(db_column='relationship_id')
    relationship_type = ForeignKeyField(db_column='relationship_type_id', rel_model=relationship_types, to_field='relationship_type')
    right_identifier = ForeignKeyField(db_column='right_identifier_id', rel_model=identifiers, related_name='identifiers_right_identifier_set', to_field='identifier')

    class Meta:
        database = spdxdb

