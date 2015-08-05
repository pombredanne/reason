import os
import subprocess
    

def initiateScan(appName, fileName):
    command = 'dependency-check/bin/dependency-check.sh --app {appName}  --scan target/dependency/ --noupdate --format XML'.format(appName = appName)
    print command
    subprocess.call(command.split(" "))
    print "done"
    print"Renaming file to {fileName}".format(fileName=fileName)
    os.rename("dependency-check-report.xml", str(fileName)+".xml")

if __name__ == '__main__':
    initiateScan("No App Name", "No File Name")
