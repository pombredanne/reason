from spdxModel import packages, files
from spdxModel licenses, packages_files, files_licenses

x = packages.select(packages.comment, licenses.short_name, packages.sha1).join(packages_files, on=packages_files.package_id).join(files,on=packages_files.file_id).join(files_licenses, JOIN.LEFT_OUTER, on=files_licenses.file_id).join(licenses, on=files_licenses.license_id).naive()


