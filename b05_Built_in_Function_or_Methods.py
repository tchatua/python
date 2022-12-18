#!/usr/bin/python3
"""
Built-in Functions: print()  str()  input()  len()
Python String Methods: find()  values()  keys()
    URL: https://www.w3schools.com/python/python_ref_functions.asp
"""
# String Built in Methods/Functions
message = "corona vaccine is ready to use, most of them are more than 90% effective"
"""
print(f"\n{message}")
print(f"1 {message.capitalize()}")
Message = message.capitalize()
print(f"2 {Message}")

#
# dir() function
print(f"\n1 ", dir(Message))
print(f"\n2 ", dir(""))
print(f"\n3 ", dir([]))
print(f"\n4 ", dir(()))
print(f"\n5 ", dir({}))
# 
print(f"3 {message.upper()}")
print(f"4 {message.islower()}")
print(f"5 {message.isupper()}")
#
print(f"6 {message.find('ready')}")# return number here is the index value where the world start
print(f"7 {message[18:24]}")
print(f"8 {message.find('not')}")# will return -1 because not is not find
#
seq1 = ("192", "168", "40", "90")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))
# List
mountains = ["Everest", "Himalaya", "Sahyadri", "Alps", "K2", "Mt Hood"]
mountains.append('Oregon mount')
print(f"\n{mountains}")
mountains.extend(["Mt Rainer", "Satpuda"])
print(f"\n{mountains}")
mountains.insert(2, "Mt Abu")
print(f"\n{mountains}")
mountains.pop() # To remove the last one
print(f"\n{mountains}")
mountains.pop(5) # To remove the 5th one
print(f"\n{mountains}")
"""
#
contract_employee_1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
print(contract_employee_1.keys())
print(contract_employee_1.values())
contract_employee_1.clear()
print(contract_employee_1)

