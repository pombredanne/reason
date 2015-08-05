import xmltodict
import re, sys

def expand(xml, properties):
    
    for key in properties:   
        if properties[key] is not None:
            xml = xml.replace('${' + key + '}', properties[key])
    return xml


def xmlparser(xmlfile):
    xmldoc = open(xmlfile, 'r')
    xmlcont = xmldoc.read()
    xmldoc.close()
    tree = xmltodict.parse(xmlcont)
    #print tree
    #checktree(tree)
    if(tree.get('project')):
        if(tree['project'].get('properties')):
            properties = tree['project']['properties']
            xmlcont = expand(xmlcont, properties)
            tree = xmltodict.parse(xmlcont)

    if(tree.get('project')):    
        dependencies = tree['project']['dependencies']
    else:
        dependencies = tree['dependencies']
    
    mav_coords = []
    for item in dependencies['dependency']:
        
        mav = str(item['groupId']) + ":" + str(item['artifactId']) + ":" + str(item['version'])
	mav_coords.append(mav)

    return(mav_coords)

if __name__ =='__main__':

    xmlparser('pom.xml')
    
