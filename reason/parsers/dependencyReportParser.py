import xmltodict
import re, sys
import itertools
from collections import OrderedDict

def dependencyReportParse(xmlfile):
    xmldoc = open(xmlfile, 'r')
    xmlcontent = xmldoc.read()
    xmldoc.close()
    

    tree = xmltodict.parse(xmlcontent)
    
    dependencies = tree['analysis']['dependencies']
    
    filename = []
    filepath = []
    sha1_hash = []
    Description = []
    license_found = []
    #evidence = [] to be added later
    #identifiers = [] to be added later
    cve = [] 
    cvssScore = []
    severity = []
    cwe = []
    description = []
    references = OrderedDict()
    cpe = OrderedDict()
    vulnerability_List = []
	
    for dependency in dependencies['dependency']:
	filename.append(dependency['fileName'])
        filepath.append(dependency['filePath'])
        sha1_hash.append(dependency['sha1'])
	Description.append(dependency.get('description', ""))
	license_found.append(dependency.get('license', ""))
	
	    	

        if 'vulnerabilities' in dependency.keys():
            temp = dependency['vulnerabilities']['vulnerability']
            if type(temp) == list:
		vulnerability_List.append(temp)
		print temp[1]
		continue
	    elif type(temp) == OrderedDict:
		print temp['name']
	else:   
	    vulnerability_List.append([])
	
     


''' 
	    cvssScore.append(temp['severity'])	
            severity.append(temp['severity'])
            cwe.append(temp['cwe'])
            description.append(temp['description'])  
    	    if "vulnerableSoftware" in temp.keys():
            	cpe[temp['name']] = temp['vulnerableSoftware']['software']
            else:
	        cpe[temp['name']] = ['No Vulnerable Software']
            if "references" in temp.keys():
	        references[temp['name']] = temp['references']['reference']    
            else:
	        references[temp['name']] = ["No References found, Fishy!"]


        else:
	    
            cve.append("No CVE Found")
            cvssScore.append("No CSVVScore Found")
            severity.append("No Severity Found")
            cwe.append("No CWE Information")
            description.append("No Description available")
            cpe[dependency['fileName']] = "No CPE for the file"
            references[dependency['fileName']] = "No references for the file"
'''	
	


if __name__ == '__main__':
    dependencyReportParse('dependency-check-report.xml')
