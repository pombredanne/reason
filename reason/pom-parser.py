#!/usr/bin/env python2
import xmltodict
import re
import sys

def expand(xml, properties):
    for key in properties:
        xml = xml.replace('${' + key + '}', properties[key])
    return xml


path = sys.argv[1]
xml = None

with open(path) as f:
    xml = f.read()
    tree = xmltodict.parse(xml)

properties = tree['project']['properties']
newxml = expand(xml, properties)

tree = xmltodict.parse(newxml)
names = []

for item in tree['project']['dependencies']['dependency']:
    name = item['groupId'] + ':' + item['artifactId'] + ' ' + item['version']
    names.append(name)

for name in sorted(names):
    print name
