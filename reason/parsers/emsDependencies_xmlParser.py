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
import dependencyScan
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
	dependencyScan(g, a, v)
	print("Done Scanning")
	#print("sleep for four seconds")
        #time.sleep(4)
    xmlParsed.close()
  




if __name__ == "__main__":
    parseXML('ems_dependencies.xml')
    print("Quitting! Bye bye ;-\)")
