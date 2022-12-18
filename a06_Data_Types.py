#!/usr/bin/python3
# Strings
str1 = "alpha"
str2 = 'beta'
str3 = """gama string"""
str4 = '''delta string'''
# Numbers
num1 = 123
num2 = 2.0
# List / Collection of multi data types, enclosed in square brackets.(Mutable)
first_list = [str1, "DevOps", 47, num1, 1.5]
# Printing a list
print(f"\n{first_list}")
# Tuples / Collection of multi data types, enclosed in round brackets.(Immutable)
first_tuple = (str1, "DevOps", 47, num1, 1.5)
print(f"{first_tuple}")
# Dictionary / Elements in the dictionary are always in pairs(key:value), curly brackets 
first_dictionary = {"Name":"Tchatua", "Weight":75, "Exercises":["Boxing", "Dancing", "Jogging"]}
print(f"{first_dictionary}")
# Type
print(f"\nVariable first_list is: {type(first_list)}")
print(f"Variable first_tuple is: {type(first_tuple)}")
print(f"Variable first_dictionary is: {type(first_dictionary)}")
# Boolean
x = True
y = False
# Printing Boolean
print(f"\n{x}, {type(x)}")
print(f"{y}, {type(y)}")




