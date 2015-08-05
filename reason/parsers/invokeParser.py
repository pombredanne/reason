'''
Author: Sai Uday Shankar
'''
from xml2mavenArtifact import xmlmvnparser
from create_pom_xml import create_pom_xml
from useDependency import initiateScan
from invokeMaven import invokeMaven
import datetime


###
# passxmlfile takes an xml file and passes it to xmlmvnparser in xml2mavenArtifact.py
#
# xmlmvnparser takes an xml file and return back maven co-ordinates 
# This return values are then passed to create a new xml file "pom.xml"
#
# Wait! What? Create pom.xml? What if I pass a pom.xml? 
# pom.xml usually has other parameters associated with it like WEB/INF
# So what? The idea behind this project at copying maven dependencies in to a folder 
# for further analysis using dependency-check i.e. get CVEs associated with dependenies
# Than just getting CVEs and CPEs, The project goes ahead with associated CWEs and
# exploring exploit-database for more information
#
# create_pom_xml from create_pom_xml.py
# This function converts given maven co-ordinates into pom.xml 
# create_pom_xml takes six(6) parameters
# A groupID - something like com.yourcompanyname
# An ArtifactID - Something like MyHelloWorldProject
# A version number - It must be like 1.0.0-SNAPSHOT
# Version number can e anythin like 1.2.3.4.5. Specify -SNAPSHOT after the version
# g, a, v are to be passed as python-list
#
# initiateScan from useDependency.py
# initiateScan takes two inputs - appName and fileName
# appName and fileName can be the same
# appName creates a unique name for the dependency-check scan
# fileName renames dependency-check-report into the name specified
# 
# invokeMaven from invokeMaven.py
# invokescan takes no inputs and runs two maven commands 
# The first is maven clean chained with compile and package - Build a jar or war or ear
# The second is to copy dependencies to "target/dependency"
#
# Order of execution
# 1. Create pom.xml and list dependencie
# 2. Invoke Maven to copy dependencies
# 3. Initiate Dependency-Check scan on the dependencies copied
###

def passxmlfile(xmlfile):
    return xmlmvnparser(xml=xmlfile)
    
mvnCoords = pasxmlfile(xml)

def invokeParser(mvnCoords):

    # Passing these values to create_pom_xml
    create_pom_xml(project_groupID = str(project_groupID), 
                   project_artifactID=str(project_artifactID),
                   project_version = str(project_version),
                   g = g,
                   a = a,
                   v = v)
    
    # Invoke Maven Commands
    invokeMaven() 
    

    # Variables for initiateScan
    date = datetime.now()
    scanVar = str(project_groupID) + str(project_artifactID) + str(date)

    # Initiate dependency-scan
    initiateScan(appName=scanVar, fileName=scanVar)





    

   
