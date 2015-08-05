import subprocess

def now():
    cmd = "python vfeedcli.py update"
    subprocess.call(cmd.split(" "))
    print("Vulnerabilities and Exploits Updated")
