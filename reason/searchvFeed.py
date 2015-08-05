from inputSanitize import cpeInfoSanitize, cveInfoSanitize
import re
from vfeed.vfeed import vFeed
import os


class searchText:
    def __init__(self):
	self.storage = []

    def searchText(self, searchtext):
	if re.match('cpe:/a:', searchtext):
	    cleanse = cpeInfoSanitize()
	    result = cleanse.cleanseCPE(searchtext)
	    if result == "Pass":
		cpe = searchtext
		#currentdir = os.getcwd()
		#changedir = currentdir +"/reason/vfeed/"
		#os.chdir(changedir)
		try:
		    vfeed = vFeed(cpe)
		    toRet = vfeed.get_cpe2cve()
		    return toRet
		except Exception as e:
		    # Log the error
		    print(e)
		#os.chdir(currentdir)		
	    else:
		return None
	

	elif re.match('CVE-', searchtext):
	    cleanse = cveInfoSanitize()
	    result = cleanse.cleanseCVE(searchtext)
	    if result == "Pass":
		cve = searchtext
		#currentdir = os.getcwd()
		#changedir = currentdir+"/reason/vfeed/"
		#os.chdir(changedir)
		try:
		    vfeed = vFeed(cve)
		    toRet = vfeed.get_cve()
		    return toRet
		except Exception as e:
		    #Log the error
		    print(e)
	 	    return None

		#os.chdir(currentdir)
		
	    else:
		return None
	else:
	    return None

