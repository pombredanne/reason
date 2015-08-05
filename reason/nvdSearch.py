from datetime import datetime
from sqlalchemy import desc
from reason import db

class cpe(db.Model):
    __bind_key__ = 'nvdDb'
    cpe_id = db.Column(db.Integer, primary_key=True)
    cpe_text = db.Column(db.Text, nullable=False)
    part = db.Column(db.Text, nullable=False)
    vendor = db.Column(db.Text, nullable=False)
    product = db.Column(db.Text, nullable=False)
    version = db.Column(db.Text, nullable=False)
    update_date = db.Column(db.Text, nullable=False)
    edition = db.Column(db.Text, nullable=False)
    language = db.Column(db.Text, nullable=False)
    
    @staticmethod
    def topcpe(num):
	return cpe.query.order_by(desc(cpe.cpe_id)).limit(num)  

    def __repr__(self):
	return "'{}''{}' '{}' '{}' '{}' '{}' '{}' '{}' '{}'".format(self.cpe_id, self.cpe_text, self.part, self.vendor, self.product, self.version, self.update_date, self.edition,self.language)


class vulnerabilities(db.Model):
    __bind_key__ = 'nvdDb'
    vuln_id = db.Column(db.Integer, primary_key=True)
    cve = db.Column(db.Text, unique = True)
    cvss_score =db.Column(db.Float)
    cwe = db.Column(db.Text)
    summary = db.Column(db.Text)
    published_date = db.Column(db.Integer)
    modified_date = db.Column(db.Integer)

    def __repr__(self):
	return "'{}' '{}' '{}' '{}' '{}' '{}' '{}'".format(self.vuln_id, self.cve, self.cvss_score, self.cwe, self.summary, self.published_date, self.modified_date)
    

class affects_to_cpe(db.Model):
    __bind_key__ = 'nvdDb'
    affects_to_cpe_id = db.Column(db.Integer, primary_key=True)
    vuln_id = db.Column(db.Integer)
    cpe_id = db.Column(db.Integer)
    
    
    def __repr__(self):
	return "'{}' '{}' '{}'".format(self.affects_to_cpe_id, self.vuln_id, self.cpe_id)
      

class sqlite_sequence(db.Model):
    __bind_key__ = 'nvdDb'
    name = db.Column(db.Text, primary_key=True)
    seq = db.Column(db.Integer)
    
    def __repr__(self):
	return "'{}' '{}'".format(self.name, self.seq)


class download_dates(db.Model):
    __bind_key__ = 'nvdDb'
    dldate_id = db.Column(db.Integer, primary_key=True)
    download_link = db.Column(db.Text)
    feed_year = db.Column(db.Text)
    feed_size = db.Column(db.Float)
    last_download = db.Column(db.Integer)

    def __repr__(self):
	return "'{}' '{}' '{}' '{}' '{}'".format(self.dldate_id, self.download_link, self.feed_year, self.feed_size, self.last_download)
    
