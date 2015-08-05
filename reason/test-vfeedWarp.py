from vfeedWarp import search


print search('cpe:/a:prosody:prosody:0.6.0', 'cve')

#print "Searching for CPE on CVE-2011-1234"

print search('CVE-2011-1234', 'cpe')

#print "Search CWE - Weakness identification on CVE-2014-2206"
print search('CVE-2014-2206', 'cwe')

#print "Search exploit database for CVE-2014-2206"
print search('CVE-2014-2206', 'exp')
