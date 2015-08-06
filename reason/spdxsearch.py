from spdxModel import packages, files
from spdxModel import licenses, packages_files, files_licenses
import json
from peewee import JOIN, fn
from pprint import pprint
from itertools import groupby
from collections import namedtuple

FoundLicense = namedtuple('FoundLicense', ['short_name', 'name', 'found_count'])


def spdxsearch(package_ids):
    x = (
        packages.select(
            packages.package_id,
            packages.name,
            packages.version,
            packages.comment,
            licenses.short_name,
            fn.Count(licenses.short_name).alias('license_found_count'),
            packages.sha1,
            licenses.name.alias('full_name')
            )
        .join(packages_files, on=packages_files.package_id)
        .join(files,on=packages_files.file_id)
        .join(files_licenses, JOIN.LEFT_OUTER, on=files_licenses.file_id)
        .join(licenses, on=files_licenses.license_id)
        .group_by(packages.package_id, packages.name, packages.version, packages.comment, licenses.short_name, packages.sha1, licenses.name)
        .order_by(packages.package_id, packages.name)
        .where(packages.package_id.in_(package_ids))
        .naive()
        )

    data = []
    for row in x:
        cpe_data = json.loads(row.comment or '[]')
        cpe = [item for item in cpe_data if item['sha1'] == row.sha1]
        # cpe = [{'cpes': sdfsdfsdf, 'sha1': sdfsdfsdff'}] or []
        if cpe:
            [cpe] = cpe
            row_data = {
                'package_id': row.package_id,
                'name': row.name,
                'version': row.version,
                'cpes': cpe['cpes'],
                'license_short_name': row.short_name,
                'license_full_name': row.full_name,
                'license_found_count': row.license_found_count
                }
            data.append(row_data)
    data.sort(key=lambda x: (x['package_id'], x['name'], x['version'], x['cpes']))
    newdata = []
    for key, group in groupby(data, lambda x: (x['package_id'], x['name'], x['version'], x['cpes'])):
        #print(key)
        newrow = {
            'package_id': key[0],
            'name': key[1],
            'version': key[2],
            'cpes': key[3],
            'licenses': [
                FoundLicense(
                    thing['license_short_name'],
                    thing['license_full_name'],
                    thing['license_found_count'],
                    )
                for thing in group
                ]
            }
        newdata.append(newrow)
    return newdata

