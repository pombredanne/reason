# pom-dependency

####### Create pom.xml dynamically using python, resolve the dependencies as jars to current folder
1. This projec may be helpful when you have a list of maven artifacts that you want to use in your java project and want to download the dependencies into a local folder instead of using maven

####### Usage:
create_pom_xml.py accepts the following values into the function create_pom_xml

1.Project Group ID - As String
2. Project Artifact ID  - As String
3. Project Version - As string
4. These values will serve purpose in creating project values in pom.xml
5. Same values will serve in creating jar file after sucessful build with pom.xml
6. g is maven group ID as a list even if passing a single item
7. a is maven artifact ID as a list even if passing a single item
8. v is maven group ID as a list even if passing a single item
9. g,a,v are maven coordinates

####### Trying out:
1. In python repr, type python test_create_pom.py.
2. A pom.xml is created with the maven coordinates passed by calling the function.
3. Compile a new list from sources to create pom.xml that meet your criteria

####### Resolving dependencies to current directory
1. For windows users, use the pom_dependencies.bat file. Double-click or run the filename with extention in command prompt. Ensure that the pom.xml is in the same directory as the batch file
2. For Users running on Linux Ubuntu, run the pom_dependencies.sh (Ensure permissions to execute the file). Ensure that pom.xml is in the same directory as the pom_dependencies.sh script

####### Making changes
1. Rename the variables in the test script if you continue using the test script
2. Importing and using the create_pom_xml from python repr or another program is easier than depending on the test script
 
