'''
Author: Sai Uday Shankar
'''
import subprocess

def invokeMaven():
    #Performing clean first
    mvn_ccp = "mvn clean"
    # Copying dependencies and transitive dependencies into "target/dependency" into a variable
    mvn_copy = "mvn install dependency:copy-dependencies -Dtransitive=true"
    #Calling the maven invocations from the variables above
    subprocess.call(mvn_ccp.split(" "))
    subprocess.call(mvn_copy.split(" "))

    print("[Info] Maven Invocation done")

if __name__ == '__main__':
    invokeMaven()
