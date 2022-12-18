#!/usr/bin/python3
"""
This script will implement our knowledge on conditions and different datatypes
This script will be interactive
"""
print(f"\nThis IT Organization has various skill sets.")
print(f"Find out your match")
print(f"Enter Capitalized Values: ")

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers","Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
contract_employee_1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
contract_employee_2 = {"Name":"Rocky", "Skill":"AI", "Code":1218}

user_skill = input("\nEnter your desire skill: ")
# print(f"{user_skill}")

# Check in the database if we have this skill
if user_skill in DevOps:
    print(f"We have {user_skill} in DevOps Team.")
elif user_skill in Development:
    print(f"We have {user_skill} in Development Team.")
elif user_skill in contract_employee_1.values() or user_skill in contract_employee_2.values():
    print(f"We have contract employees with this skill")
else:
    print(f"Skill not found")
    print(f"Please check if you have entered value in capitalize or check the spelling")
    
    
    
    





