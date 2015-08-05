'''
Author: Sai Uday Shankar
'''
from xml2mavenArtifact import whatinxml
from create_pom_xml import create_pom_xml
from useDependency import initiateScan
from invokeMaven import invokeMaven
from datetime import datetime


###
# passxmlfile takes an xml file and passes it to xmlmvnparser, but first goes through whatinxml() 
# in xml2mavenArtifact.py
#
# whatinxml() takes an xml file and tries to check for version numbers written as variables for maven g,a,v co-ords
# A quick replacement is done if present and then sent to xmlmvnparser
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
    mvnCoords = whatinxml(xmlfile)
    invokeParser(mvnCoords)
    

def invokeParser(mvnCoords):

    # Passing these values to create_pom_xml
    create_pom_xml(*mvnCoords)
    
    # Invoke Maven Commands
    invokeMaven() 
    

    # Variables for initiateScan
    d = datetime.now()
    appendDate = datetime.strftime(d, '%d:%m:%y:%H:%M:%S')
    scanVar = mvnCoords.pGroupId + mvnCoords.pArtifactId + mvnCoords.pArtifactId + appendDate
    # Initiate dependency-scan
    initiateScan(appName=scanVar, fileName=scanVar)


if __name__ == '__main__':
    passxmlfile('pom.xml')


    

   
