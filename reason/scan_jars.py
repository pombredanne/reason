#!/usr/bin/env python2

from __future__ import print_function

import re
import os
import subprocess
import sys


def scan_jars(directory):
    last_seen = None
    packages = []

    for subdir, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".jar") and '/.nexus/' not in subdir:
                packages.append((os.path.splitext(filename)[0], os.path.join(subdir, filename)))
                continue

    package_ids = set()

    for package_name, package_path in sorted(packages):
        args = [
            'dosocs2', 'scan',
            '--scanners', 'nomos_deep,dependency_check',
            '--package-name', '-'.join(package_name.split('-')[:-1]),
            '--package-version', package_name.split('-')[-1],
            package_path
            ]
        try:
            output = subprocess.check_output(args, stderr=subprocess.STDOUT)
            print(output)
            m = re.match(r'.*package_id: ([0-9]+)', output)
            if m:
                package_id = m.group(1)
                package_ids.add(int(package_id))
        except subprocess.CalledProcessError:
            pass
    return package_ids
