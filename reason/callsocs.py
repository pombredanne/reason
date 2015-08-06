from xml2mavenArtifact import xmlparser
from create_pom_xml import create_pom_xml
import itertools
from invokeMaven import invokeMaven
from scan_jars import scan_jars
from spdxsearch  import spdxsearch
from vfeedWarp import search

import tempfile
import os
import shutil
from contextlib import contextmanager
import subprocess

@contextmanager
def TemporaryDirectory():
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path, ignore_errors=True)


@contextmanager
def ChDir(new_dir):
    old_dir = os.getcwd()
    os.chdir(new_dir)
    yield
    os.chdir(old_dir)


def callsocs(xmlfile):
    print "[+] starting"
    with TemporaryDirectory() as workdir:
        shutil.copyfile(xmlfile, os.path.join(workdir, 'pom.xml'))
        print "[+] Created pom.xml"
        with ChDir(workdir):
            subprocess.check_call(['mvn', 'dependency:copy-dependencies'])
        print "[+] Maven Invocation done"
        package_ids = list(scan_jars(os.path.join(workdir, 'target/dependency')))
    spdx_query_results = spdxsearch(package_ids) 
    print "[+] DoSocs2 and Dependency-Check Done"
    for item in spdx_query_results:
        cves = []
        for cpe in item['cpes']:
            cves.append(search(cpe['cpe'], 'cve'))
        item['cves'] = cves
    return list(sorted(spdx_query_results, key=lambda x: (x['name'], x['version'])))
