from xml2mavenArtifact import xmlparser
from create_pom_xml import create_pom_xml
import itertools
from invokeMaven import invokeMaven
from scan_jars import scan_jars
from spdxsearch  import spdxsearch
from vfeedWarp import search

def callsocs(xmlfile):
    print "[+] starting"

    project_groupID = "com.ushan"
    project_artifactId = "HelloWorld"
    project_version = "1.0.0-SNAPSHOT"

    g, a, v = xmlparser(xmlfile)
    
    print "[+] Parsing done"
    create_pom_xml(project_groupID, project_artifactId, project_version, g, a, v)
    print "[+] Created pom.xml"
    invokeMaven()
    print "[+] Maven Invocation done"
    package_ids = list(scan_jars('target/dependency'))
    spdx_query_results = spdxsearch(package_ids) 
    print "[+] DoSocs2 and Dependency-Check Done"
    print "[+] Sorting for results"
    #return spdx_query_results
    sort_results = spdxsort(spdx_query_results)
    return sort_results

#def all_cpes(spdx_query_results):
#    for item in spdx_query_results:
#        for item in result['cpes']:
#            yield (result['package_id'], item['cpe'])

def spdxsort(results):
    
    package_id = []
    name = []
    version = []
    licenses = []
    cpe_pkg = []
    cpe_list =[]
    cves = []
   
#    for result in spdx_query_results:
#        name.append(result['name'])
#        package_id.append(result['package_id'])
#        version.append(result['version'])
#        licenses.append(result['licenses']) 
        
    for i in range(len(results)):
        if results[i]['cpes']:
            for item in results[i]['cpes']:
                cpe_list.append(item.values()[1])
                cpe_pkg.append(results[i]['package_id'])
                cves.append(search(str(item.values()[1]), 'cve'))
                #printing CPEs
                print str(item.values()[1])
        else:
            cpe_pkg.append([])
            cpe_list.append([])
            cves.append([])

        name.append(results[i]['name'])
        package_id.append(results[i]['package_id'])
        version.append(results[i]['version'])
        licenses.append(results[i]['licenses'])

    return([package_id, name, version, licenses, cpe_pkg, cpe_list, cves])



        



    













