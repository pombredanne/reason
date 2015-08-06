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
    for item in spdx_query_results:
        cves = []
        for cpe in item['cpes']:
            cves.append(search(cpe['cpe'], 'cve'))
        item['cves'] = cves
    return spdx_query_results

