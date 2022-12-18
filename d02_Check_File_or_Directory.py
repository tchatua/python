#!/usr/bin/python3
import os

# path = "/opt/a01_scriptbox"
path = "/tmp/testfile.txt"

if os.path.isfile(path):
    print("It's a file")
elif os.path.isdir(path):
    print("It's a Directory")
else:
    print("File or Directory don't exist")
    



