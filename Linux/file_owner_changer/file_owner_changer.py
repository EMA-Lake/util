import os
import sys
import subprocess

name = sys.argv[1]

for path, subdirs, files in os.walk('.', topdown=False):
    for file in files:
        subprocess.call(['sudo', 'chown', '-R', name, os.path.join(path, file)])
    for subdir in subdirs:
        subprocess.call(['sudo', 'chown', '-R', name, os.path.join(path, subdir)])