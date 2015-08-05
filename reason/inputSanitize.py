import re
import itertools

class cpeInfoSanitize:
    
    def __init__(self):
	self.storage = []
    
    def cleanseCPE(self, cpeInfo):
        cpeInput = str(cpeInfo).lower()
	sergey = re.compile('cpe:/a:[a-zA-Z0-9:_-]*')
	if sergey.match(cpeInput):	
	    # Calling search on CPE
	    return "Pass"
	else:
	    #return "[Error] Please check your input"
	    return "Fail"

class cveInfoSanitize:

    def __init__(self):
        self.storage = []

    def cleanseCVE(self, cveInfo):
	cveInput = str(cveInfo).upper()
	sergey = re.compile('CVE-[0-9]*-[0-9]*')
	if sergey.match(cveInput):
	    return "Pass"
	else:
	    return "Fail"

class plainTextInfoSanitize:

    def __init__(self):
	self.storage = []

    def cleansePlainText(self, plainTextInfo):
        plainInput = str(plainTextInfo)
	sergey = re.compile(r'[a-zA-Z0-9:/\-\_]*')
	if serget.match(plainInput):
	    return "Pass"
	else:
	    # Perform No Search
	    return "Fail"


class riskInfoSanitize:

    def __init__(self):
	self.storage = []

    def cleanRisk(self, riskInfo):
	riskInput = str(riskInfo)
	

