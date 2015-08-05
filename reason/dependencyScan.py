'''
Author: Sai Uday Shankar 
Email: skorlimarla@unomaha.edu
'''
import time, subprocess
import shutil
from StringIO import StringIO
import itertools
import re, os




def dependencyScan(g, a, v):
    print("Starting scan on {g} {a} {v}".format(g=g, a=a, v=v))
    mvncmd = 'mvn org.apache.maven.plugins:maven-dependency-plugin:2.4:get -DgroupId={g} -DartifactId={a} -Dversion={v} -Dtransitive=true'.format(g=g, a=a, v=v)
    subprocess.call(mvncmd.split(" "))
    #os.system(mvncmd)
    print("Finished a dependency check sub routine on {g} {a} {v}".format(g=g, a=a, v=v))

    #Removing - Reuse over iteration - To prevent duplicates
    mvnCmd = ""
    depParams = "/home/skorlimarla/projects/projects/reason/dependency-check/bin/dependency-check.sh --noupdate --app \"{g}{a}{v}\" --scan /home/skorlimarla/.m2".format(g=g, a=a, v=v)
    print(depParams)
    subprocess.call(depParams.split(" "))
    depParams = ""
    os.rename("dependency-check-report.html", "{g}{a}{v}.html".format(g=g, a=a, v=v))
        # We rebuild dependencies for each run - Each package dependencies can be clearly observed this way
        # To Add Dependency Graph here - Future Work
    shutil.rmtree('/home/skorlimarla/.m2')



def dependencyScanDir(dirname, packname):
    print("Starting scan on {}".format(str(dir)))
    
    scannerPath = "/home/skorlimarla/projects/projects/reason/dependency-check/bin/dependency-check.sh --format XML --out . --noupdate "
    packagename = str("--app " + packname)
    packRename = str(packname + ".xml")
    directory = str(" --scan " + dirname)
    depParams = scannerPath + packagename + directory
    print(depParams)
    subprocess.call(depParams.split(" "))
    depParams = ""
    os.rename("dependency-check-report.xml", packRename)
        # We rebuild dependencies for each run - Each package dependencies can be clearly observed this way
        # To Add Dependency Graph here - Future Work





if __name__ == '__main__':
    dependencyScan(g, a, v)
