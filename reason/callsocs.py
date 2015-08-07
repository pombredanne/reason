import itertools
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


def callsocs(workdir, xmlfile):
    print "[+] starting"
    os.rename(xmlfile, os.path.join(workdir, 'pom.xml'))
    print "[+] Created pom.xml"
    with ChDir(workdir):
        subprocess.check_call(['mvn', 'dependency:copy-dependencies'])
    print "[+] Maven Invocation done"
    package_ids = list(scan_jars(os.path.join(workdir, 'target/dependency')))
    spdx_query_results = spdxsearch(package_ids) 
    print "[+] DoSocs2 and Dependency-Check Done"
    for item in spdx_query_results:
        cves_cvss = []
        for cpe in item['cpes']:
            cves = search(cpe['cpe'][1:-1], 'cve')
            #cvss_score = search(cve, 'cvss')
            for cve in cves:
                if cve:
                    cvss_score = search(cve, 'cvss')
                print (cve, cvss_score)
                cves_cvss.append((cve, cvss_score))
        item['cves'] = cves_cvss

    return list(sorted(spdx_query_results, key=lambda x: (x['name'], x['version'])))
