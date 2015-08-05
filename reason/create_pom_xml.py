'''
Author: Sai Uday Shankar, Korlimarla
Create pom.xml from list of maven artifacts with python
'''

##### Pass the following values into this function
## Project Group ID - As String
## Project Artifact ID  - As String
## Project Version - As string
## These values will serve purpose in creating project values in pom.xml
## Same values will serve in creating jar file after sucessful build with pom.xml
## g is maven group ID as a list even if passing a single item
## a is maven artifact ID as a list even if passing a single item
## v is maven group ID as a list even if passing a single item
#####

from xml.dom import minidom
import itertools

def create_pom_xml(project_groupID, project_artifactID, project_version, g,a,v):
    doc = minidom.Document()
    root = doc.createElement('project')
    doc.appendChild(root)

    modelVersion = doc.createElement('modelVersion')
    text = doc.createTextNode('4.0.0')
    modelVersion.appendChild(text)
    root.appendChild(modelVersion)

    groupId = doc.createElement('groupId')
    text = doc.createTextNode(project_groupID)
    groupId.appendChild(text)
    root.appendChild(groupId)

    artifactId = doc.createElement('artifactId')
    text = doc.createTextNode(project_artifactID)
    artifactId.appendChild(text)
    root.appendChild(artifactId)

    version = doc.createElement('version')
    text = doc.createTextNode(project_version)
    version.appendChild(text)
    root.appendChild(version)

    dependencies = doc.createElement('dependencies')
    root.appendChild(dependencies)


    for g_val, a_val, v_val in itertools.izip(g, a, v):

        dependency = doc.createElement('dependency')

        dep_group = doc.createElement('groupId')
        text = doc.createTextNode(g_val)
        dep_group.appendChild(text)
        dependency.appendChild(dep_group)

        dep_artifact = doc.createElement('artifactId')
        text = doc.createTextNode(a_val)
        dep_artifact.appendChild(text)
        dependency.appendChild(dep_artifact)

        dep_version = doc.createElement('version')
        text = doc.createTextNode(v_val)
        dep_version.appendChild(text)
        dependency.appendChild(dep_version)
        
        dependencies.appendChild(dependency)
        root.appendChild(dependencies)


    xml_str = doc.toprettyxml(indent="  ")
    with open("pom.xml", "w") as f:
        f.write(xml_str)

