'''
Author: Sai Uday Shankar
Email: skorlimarla@unomaha.edu
'''

from StringIO import StringIO
from lxml import etree
import itertools
import re, os
import subprocess
from subprocess import Popen, PIPE
import shutil
import time

# ems_depencencies.xml - XML Parser, Dependecy Check Scanner, Dependency Report Parser


groupId = []
artifactId = []
version = []


def parseXML(xmlFile):
    '''
    XML Dependencies Parser
    '''
    xmlOpen = open(xmlFile)
    xml = xmlOpen.read()
    xmlOpen.close()
    tree = etree.parse(StringIO(xml))
    content = etree.iterparse(StringIO(xml))

    print("XML Parsing started")

    for action, element in content:
        if not element.text:
            element.text = "None"
	elif element.tag == "dependency" :
	    element.tag = "None"
	elif element.tag == "dependencies":
	    element.tag = "None"
        else:
	    if(element.tag == "groupId"):
		groupId.append(element.text)
	    elif(element.tag == "artifactId"):
		artifactId.append(element.text)
	    elif(element.tag == "version"):
		version.append(element.text)
	    elif(element.tag == "scope"):
		continue
	    else:
		print("There is a change XML being parsed")

    print("xml Parsing completed")
    xmlParsed = open('xmlParsed.txt', 'w')
    for g, a, v in itertools.izip(groupId, artifactId, version):
        xmlParsed.write(g+'::'+a+'::'+v+'\n')
	print("Running Dependencycheck for {gid} :: {aid} :: {ver}".format(gid=g, aid=a, ver=v))
	mvncmd = 'mvn org.apache.maven.plugins:maven-dependency-plugin:2.4:get  -DgroupId={g} -DartifactId={a} -Dversion={v}'.format(g=g, a=a, v=v)
	os.system(mvncmd)
	dependencyScan(g, a, v)
	print("Done Scanning")
	print("sleep for four seconds")
        time.sleep(0)
    xmlParsed.close()
     

def dependencyScan(g, a, v):
    print("Starting scan on {g} {a} {v}".format(g=g, a=a, v=v))
    #mvncmd = 'mvn org.apache.maven.plugins:maven-dependency-plugin:2.4:get  -DgroupId={g} -DartifactId={a} -Dversion={v}'.format(g=g, a=a, v=v)
    #p = subprocess.Popen(mvncmd, shell=True, stdout=subprocess.PIPE)
    #os.system(mvncmd)
    print("Finished a dependency check sub routine on {g} {a} {v}".format(g=g, a=a, v=v))
    #subprocess.call([mvncmd])
    #Removing - Reuse over iteration - To prevent duplicates
    #mvnCmd = ""
    
    depParams = "/home/skorlimarla/projects/projects/reason/dependency-check/bin/dependency-check.sh --noupdate --app \"{g}{a}{v}\" --scan /home/skorlimarla/.m2".format(g=g, a=a, v=v)
    #print(depParams)
    os.system(depParams)
    #depParams = ""
    #os.rename("dependency-check-report.html", "{g}{a}{v}.html".format(g=g, a=a, v=v))
        # We rebuild dependencies for each run - Each package dependencies can be clearly observed this way
	# To Add Dependency Graph here - Future Work
    #shutil.rmtree('/home/skorlimarla/.m2')

if __name__ == "__main__":
    parseXML('ems_dependencies.xml')
    print("Quitting! Bye bye ;-\)")
