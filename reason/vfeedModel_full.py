from peewee import *

database = SqliteDatabase('vfeed/vfeed.db', **{})

class TextField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class NvdDb(BaseModel):
    cveid = TextField(primary_key=True)
    cvss_access_complexity = TextField()
    cvss_access_vector = TextField()
    cvss_authentication = TextField()
    cvss_availability_impact = TextField()
    cvss_base = TextField()
    cvss_confidentiality_impact = TextField()
    cvss_exploit = TextField()
    cvss_impact = TextField()
    cvss_integrity_impact = TextField()
    date_modified = DateField()
    date_published = DateField()
    summary = TextField()

    class Meta:
        db_table = 'nvd_db'

class CveCpe(BaseModel):
    cpeid = TextField()  # name
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')

    class Meta:
        db_table = 'cve_cpe'

class CveCwe(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    cweid = TextField()  # name

    class Meta:
        db_table = 'cve_cwe'

class CveReference(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    refname = TextField()  # name
    refsource = TextField()  # name

    class Meta:
        db_table = 'cve_reference'

class CweDb(BaseModel):
    cweid = TextField()  # name
    cwetitle = TextField()  # name

    class Meta:
        db_table = 'cwe_db'

class CweCapec(BaseModel):
    capecid = TextField()  # name
    cweid = ForeignKeyField(db_column='cweid', rel_model=CweDb, to_field='cweid')

    class Meta:
        db_table = 'cwe_capec'

class CweCategory(BaseModel):
    categoryid = TextField()  # name
    categorytitle = TextField()  # name
    cweid = ForeignKeyField(db_column='cweid', rel_model=CweDb, to_field='cweid')

    class Meta:
        db_table = 'cwe_category'

class Ftsentry(BaseModel):
    foreign = TextField(db_column='FOREIGN', )  # 
    content = TextField()  # 
    entry = TextField(db_column='entry_id', )  # 

    class Meta:
        db_table = 'ftsentry'

class FtsentryContent(BaseModel):
    c0entry = TextField(db_column='c0entry_id', )  # 
    c1content = TextField()  # 
    c2foreign = TextField(db_column='c2FOREIGN', )  # 
    docid = PrimaryKeyField()

    class Meta:
        db_table = 'ftsentry_content'

class FtsentryDocsize(BaseModel):
    docid = PrimaryKeyField()
    size = BlobField()

    class Meta:
        db_table = 'ftsentry_docsize'

class FtsentrySegdir(BaseModel):
    end_block = IntegerField()
    idx = IntegerField()
    leaves_end_block = IntegerField()
    level = IntegerField()
    root = BlobField()
    start_block = IntegerField()

    class Meta:
        db_table = 'ftsentry_segdir'
        primary_key = CompositeKey('idx', 'level')

class FtsentrySegments(BaseModel):
    block = BlobField()
    blockid = PrimaryKeyField()

    class Meta:
        db_table = 'ftsentry_segments'

class FtsentryStat(BaseModel):
    value = BlobField()

    class Meta:
        db_table = 'ftsentry_stat'

class MapCveAixapar(BaseModel):
    aixaparid = TextField()  # name
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')

    class Meta:
        db_table = 'map_cve_aixapar'

class MapCveBid(BaseModel):
    bidid = TextField()  # name
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')

    class Meta:
        db_table = 'map_cve_bid'

class MapCveCertvn(BaseModel):
    certvuid = TextField()  # name
    certvulink = TextField()  # name
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')

    class Meta:
        db_table = 'map_cve_certvn'

class MapCveCisco(BaseModel):
    ciscoid = TextField()  # name
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')

    class Meta:
        db_table = 'map_cve_cisco'

class MapCveD2(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    d2_script_file = TextField()  # name
    d2_script_name = TextField()  # name

    class Meta:
        db_table = 'map_cve_d2'

class MapCveDebian(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    debianid = TextField()  # name

    class Meta:
        db_table = 'map_cve_debian'

class MapCveExploitdb(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    exploitdbid = TextField()  # name
    exploitdbscript = TextField()  # name

    class Meta:
        db_table = 'map_cve_exploitdb'

class MapCveFedora(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    fedoraid = TextField()  # name

    class Meta:
        db_table = 'map_cve_fedora'

class MapCveGentoo(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    gentooid = TextField()  # name

    class Meta:
        db_table = 'map_cve_gentoo'

class MapCveHp(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    hpid = TextField()  # name
    hplink = TextField()  # name

    class Meta:
        db_table = 'map_cve_hp'

class MapCveIavm(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    disakey = TextField()  # name
    iavmid = TextField()  # name
    iavmtitle = TextField()  # name

    class Meta:
        db_table = 'map_cve_iavm'

class MapCveMandriva(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    mandrivaid = TextField()  # name

    class Meta:
        db_table = 'map_cve_mandriva'

class MapCveMilw0Rm(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    milw0rmid = TextField()  # name

    class Meta:
        db_table = 'map_cve_milw0rm'

class MapCveMs(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    msid = TextField()  # name
    mstitle = TextField()  # name

    class Meta:
        db_table = 'map_cve_ms'

class MapCveMsf(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    msf_script_file = TextField()  # name
    msf_script_name = TextField()  # name
    msfid = TextField()  # name

    class Meta:
        db_table = 'map_cve_msf'

class MapCveMskb(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    mskbid = TextField()  # name
    mskbtitle = TextField()  # name

    class Meta:
        db_table = 'map_cve_mskb'

class MapCveNessus(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    nessus_script_family = TextField()  # name
    nessus_script_file = TextField()  # name
    nessus_script = TextField(db_column='nessus_script_id', )  # name
    nessus_script_name = TextField()  # name

    class Meta:
        db_table = 'map_cve_nessus'

class MapCveNmap(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    nmap_script_cat = TextField()  # name
    nmap_script = TextField(db_column='nmap_script_id', )  # name

    class Meta:
        db_table = 'map_cve_nmap'

class MapCveOpenvas(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    openvas_script_family = TextField()  # name
    openvas_script_file = TextField()  # name
    openvas_script = TextField(db_column='openvas_script_id', )  # name
    openvas_script_name = TextField()  # name

    class Meta:
        db_table = 'map_cve_openvas'

class MapCveOsvdb(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    osvdbid = TextField()  # name

    class Meta:
        db_table = 'map_cve_osvdb'

class MapCveOval(BaseModel):
    cpeid = TextField()  # name
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    ovalclass = TextField()  # name
    ovalid = TextField()  # name
    ovaltitle = TextField()  # name

    class Meta:
        db_table = 'map_cve_oval'

class MapCveRedhat(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    redhatid = TextField()  # name
    redhatovalid = TextField()  # name
    redhatupdatedesc = TextField()  # name

    class Meta:
        db_table = 'map_cve_redhat'

class MapCveSaint(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    saintexploitid = TextField()  # name
    saintexploitlink = TextField()  # name
    saintexploittitle = TextField()  # name

    class Meta:
        db_table = 'map_cve_saint'

class MapCveScip(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    scipid = TextField()  # name
    sciplink = TextField()  # name

    class Meta:
        db_table = 'map_cve_scip'

class MapCveSnort(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    snort_classtype = TextField()  # name
    snort = TextField(db_column='snort_id', )  # name
    snort_sig = TextField()  # name

    class Meta:
        db_table = 'map_cve_snort'

class MapCveSuricata(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    suricata_classtype = TextField()  # name
    suricata = TextField(db_column='suricata_id', )  # name
    suricata_sig = TextField()  # name

    class Meta:
        db_table = 'map_cve_suricata'

class MapCveSuse(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    suseid = TextField()  # name

    class Meta:
        db_table = 'map_cve_suse'

class MapCveUbuntu(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    ubuntuid = TextField()  # name

    class Meta:
        db_table = 'map_cve_ubuntu'

class MapCveVmware(BaseModel):
    cveid = ForeignKeyField(db_column='cveid', rel_model=NvdDb, to_field='cveid')
    vmwareid = TextField()  # name

    class Meta:
        db_table = 'map_cve_vmware'

class MapRedhatBugzilla(BaseModel):
    advisory_dateissue = TextField()  # name
    bugzillaid = TextField()  # name
    bugzillatitle = TextField()  # name
    redhatid = ForeignKeyField(db_column='redhatid', rel_model=MapCveRedhat, to_field='redhatid')

    class Meta:
        db_table = 'map_redhat_bugzilla'

class StatNewCve(BaseModel):
    new_cve = TextField(db_column='new_cve_id', )  # name
    new_cve_summary = TextField()  # name

    class Meta:
        db_table = 'stat_new_cve'

class StatVfeedKpi(BaseModel):
    db_version = TextField()  # name
    total_aixapar = TextField()  # name
    total_bid = TextField()  # name
    total_capec = TextField()  # name
    total_certvu = TextField()  # name
    total_cisco = TextField()  # name
    total_cpe = TextField()  # name
    total_cve = TextField()  # name
    total_cwe = TextField()  # name
    total_d2exploit = TextField()  # name
    total_debian = TextField()  # name
    total_exploitdb = TextField()  # name
    total_fedora = TextField()  # name
    total_gentoo = TextField()  # name
    total_hp = TextField()  # name
    total_iavm = TextField()  # name
    total_mandriva = TextField()  # name
    total_milw0rm = TextField()  # name
    total_ms = TextField()  # name
    total_msf = TextField()  # name
    total_mskb = TextField()  # name
    total_nessus = TextField()  # name
    total_nmap = TextField()  # name
    total_openvas = TextField()  # name
    total_osvdb = TextField()  # name
    total_oval = TextField()  # name
    total_redhat = TextField()  # name
    total_redhat_bugzilla = TextField()  # name
    total_saint = TextField()  # name
    total_scip = TextField()  # name
    total_snort = TextField()  # name
    total_suricata = TextField()  # name
    total_suse = TextField()  # name
    total_ubuntu = TextField()  # name
    total_vmware = TextField()  # name

    class Meta:
        db_table = 'stat_vfeed_kpi'

