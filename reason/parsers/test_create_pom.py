'''
Author: Sai Uday Shankar, Korlimarla
Sample to create pom.xml
'''


from create_pom_xml import create_pom_xml
import itertools
from xml.dom import minidom

project_groupID = "com.ushan"
project_artifactId = "HelloWorld"
project_version = "1.0.0-SNAPSHOT"

g = []
a = []
v = []

g.append("org.springframework")
g.append("commons-lang")

a.append("spring-web")
a.append("commons-lang")

v.append("4.1.4.RELEASE")
v.append("2.1")

create_pom_xml(project_groupID, project_artifactId, project_version, g, a, v)
print("done creating sample pom.xml file! Quitting")
