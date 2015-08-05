'''
Author: Sai Uday Shankar
'''
import subprocess

def invokeMaven():
    # Chaining clean compile and package on pom.xml into a variable
    mvn_ccp = "mvn clean compile package"
    # Copying dependencies and transitive dependencies into "target/dependency" into a variable
    mvn_copy = "mvn install dependency:copy-dependencies -Dtransitive=true"
    #Calling the maven invocations from the variables above
    subprocess.call(mvn_ccp.split(" "))
    subprocess.call(mvn_copy.split(" "))

    print("[Info] Maven Invocation done")
