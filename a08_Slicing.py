#!/usr/bin/python3
"""
planet_1 = "Closest of Sun"
print(f"\n{planet_1}")
print(f"\n{planet_1[0]}")
print(f"{planet_1[1]}")
print(f"{planet_1[2]}")
print(f"\n{planet_1[-1]}")
print(f"{planet_1[-2]}")
print(f"{planet_1[-3]}")
# Slicing a string, get a sub string from a string
print(f"\n{planet_1[1:4]}")
print(f"\n{planet_1[:]}")
print(f"\n{planet_1[:7]}")
print(f"\n{planet_1[11:]}")
# Slicing Tuple
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python","Ansible")
print(f"\n{devops[0]}")
print(f"{devops[4]}")
print(f"{devops[1]}")
print(f"\n{devops[2:5]}")
print(f"{devops[2:5][0]}")
print(f"\n{devops[2:5][0][5:11][-1]}")
# Slicing List
devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python","Ansible"]
print(f"\n{devops[0]}")
print(f"{devops[4]}")
print(f"{devops[1]}")
print(f"\n{devops[2:5]}")
print(f"{devops[2:5][0]}")
print(f"\n{devops[2:5][0][5:11][-1]}")
"""

# Dictionary Example
Skills ={"devops":("AWS", "Jenkins", "Python", "Ansible",), "Development":["Java", "NodeJS", "net"]}
print(f"{Skills}")
print(f"{Skills['devops']}")
print(f"{Skills['devops'][-1][:3]}")

