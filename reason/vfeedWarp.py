from vfeedModel import nvd_db, cve_cpe, cve_cwe, map_cve_exploitdb
from inputSanitize import cpeInfoSanitize, cveInfoSanitize
from inputSanitize import plainTextInfoSanitize

# Take user input here and search
def search(userInput, what_with_input):
    '''
    Search funtion expects two inputs
        1. UserInput - A string that you want to search for
           Pass a unicode or a string here
        2. What_with_input
           Pass values to perform actions
           Actions available are cpe, cve, cwe, exploit
        Usage Instances:
           A. search('cpe:/a:prosody:prosody:0.6.0', 'cve')
              Returns CVE(s) associated with the cpe given

           B. search('CVE-2011-1234', 'cpe')
              Returns CPE(s) associated with the CVE given
           
           C. search('CVE-2014-2206',exp')
               Returns exploit(s) associated with the CVE
         
           D. search('CVE-2014-2206', 'cwe')
              Returns CWE(s) associated with the CVE
    '''
    
    assert what_with_input in ['cpe', 'cwe', 'cve', 'exp']
    
    cve_verify = cveInfoSanitize()
    cpe_verify = cpeInfoSanitize()
    
    inp = userInput
    action = what_with_input
    
    result=''

    if action == 'cpe':
        result = cve_verify.cleanseCVE(inp) 
        if result == "Pass":
            result = ''
            return search_for_cpe_by_cve(inp)
        else:
            result = ''
            return []
    
    elif action == 'cve':
        result = cpe_verify.cleanseCPE(inp)

        if result == "Pass":
            result = ''
            return search_for_cve_by_cpe(inp)
        else:
            result =''
            return []

    elif action == 'cwe':
        result = cve_verify.cleanseCVE(inp)
        if result == "Pass":
            result = ''
            return search_for_cwe_by_cve(inp)
        else:
            result = ''
            return []

    elif action == 'exp':
        result = cve_verify.cleanseCVE(inp)
        if result == "Pass":
            result = ''
            return search_for_exploit_by_cve(inp)
        else:
            result = ''
            return []
    
    else:
        return []
         

# Takes cpe and gives CVEs - Product to Vulnerability 
def search_for_cve_by_cpe(cpe):
    # Call data cleanse
    cves = []
        
    for x in cve_cpe.select().join(nvd_db)   .where(cve_cpe.cpeid == cpe):
        cves.append(x.cveid_id)
    return cves
            

# Takes CVE and gives CPEs - Vulnerability tied to multiple products
def search_for_cpe_by_cve(cve):
    cpes = []
    cves = cve    
    for x in cve_cpe.select(cve_cpe.cpeid).join(nvd_db).where(nvd_db.cveid == cve):
        cpes.append(x.cpeid)
    return cpes


# Takes in CVEs and gives CWEs associated with CVEs 
def search_for_cwe_by_cve(cve):

    cwes = []

    for x in cve_cwe.select(cve_cwe.cweid).join(nvd_db).where(nvd_db.cveid ==cve):
        cwes.append(x.cweid)
    return(cwes)


        
# Takes CVEs and gives Exploit DB ID associated with the CVEs
def search_for_exploit_by_cve(cve):
    cves = []
    expid = []
    
    for x in map_cve_exploitdb.select(map_cve_exploitdb.exploitdbid).join(nvd_db).where(nvd_db.cveid == cve):
        expid.append(x.exploitdbid)
    return expid
        

if __name__ =='__main__':
    processInput(userInput, what_with_input)








