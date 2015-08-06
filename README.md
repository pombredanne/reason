# Reason

####### Project License and Vulnerability information 


####### What is in reason?
1. CPE and CVE reverse search
2. Get CWE and exploit-db information for a CVE
3. Get License & CVE information on packages as CPEs in project
4. Observe the results


####### How does one get started?
1. Install python requirements from requirements.txt
2. Download dependency-check command-line v1.2.11 from OWASP

    URL: https://www.owasp.org/index.php/OWASP_Dependency_Check

    1.3 was released yesterday but is not being consumed yet.

3. clone dosocs2 from Tom Gurney

    ```
    git clone https://github.com/ttgurney/dosocs2.git 
    ```
4. Run manage.py and initialize database for login

    ```
    python manage.py run initdb
    ```
5. Next, Getting vfeed database updates! The source for vfeed is from https://github.com/toolswatch/vFeed.git but Observe the changes made in https://github.com/Ushan89/vFeed.git

    To update vfeed:

    ```
    python manage.py update
    ```
6. Running reason is simple. 

    ```
    python manage.py runserver
    ```

    Observe that in manage.py, we have a default username & password as sai. Default port is 8095.

7. Effective URL is http://<IP Address or Domain>:8095

    The socket bind is "0.0.0.0":<portnumber>

8. Once logged-in, Check the upload section. Here you can upload xml files.

9. xml files are expected to be of the format as below

    ```
    <?xml version="1.0"?>
        <project>
        <modelVersion>4.0.0</modelVersion>
        <groupId>com.ushan</groupId>
        <artifactId>HelloWorld</artifactId>
        <version>1.0.0-SNAPSHOT</version>

        <dependencies>
            <dependency>
                <groupId>org.springframework</groupId>
                <artifactId>spring-web</artifactId>
                <version>4.1.4.RELEASE</version>
            </dependency>
            <dependency>
                <groupId>commons-lang</groupId>
                <artifactId>commons-lang</artifactId>
                <version>2.1</version>
            </dependency>
        </dependencies>
    </project>
    ```
10. The xml file may have any number of goals and other parameters, but those are ignored and only the dependencies are taken further for analysis.

11. If there are dependencies that are proprietary or internal and not available for download from maven central, fetching dependencies may fail unless the user running the manage.py script has maven settings configured to fulfill the dependencies.
    Note: All transitive dependencies are included.

12. Once upload is sucessful, user is redirected to a page where the data is now visible as a HTML table. Data cannot be exported yet but may be available in the future.

