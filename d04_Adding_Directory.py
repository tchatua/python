#!/usr/bin/python3
import os

if os.path.isdir("/opt/science_dir3"):
    print(f"\nDirectory already exist\n")
else:
    os.mkdir("/opt/science_dir3")
    print(f"\nscience_dir3 directory is created\n")

# Assigning Permission and Ownership to the Directory
print(f"Assigning Permission and Ownership to the Directory\n")
os.system("chown :science /opt/science_dir3")
os.system("chmod 770 /opt/science_dir3")