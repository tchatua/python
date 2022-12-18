#!/usr/bin/python3
# Arithmetic operators
x = 2
y = 7
total = x + y       # Addition
print(f"\n{total}")
total = x - y       # Subtraction
print(f"\n{total}")
total = x * y       # Multiplication
print(f"\n{total}")
total = x + y       # Addition
print(f"\n{total}")
total = y % x       # Modulo
print(f"\n{total}")
total = y**x        # Exponential
print(f"\n{total}")
# Comparison Operators
a = 30
b = 60
out = a < b         # Less than  
print(f"\n{out}")
out = a > b         # Greater  than
print(f"\n{out}")   
out = (a == b)      # Equal
print(f"\n{out}")
out = (a != b)      # Not equal
print(f"\n{out}")
out = (a >= b)      # Greater than or equal
print(f"\n{out}")
out = (a <= b)      # Less than or equal
print(f"\n{out}")
# Assignment operators
c = 0
d = 1
# c+=d                # c = c+d --> Incrementing
print(f"\n{c}")
c-=d                # c = c-d --> decrementing
print(f"\n{c}")
# Logical operator
a = 40
b = 60
x = 2
y = 3
# or
out = (a<b) or (x>y) # True or False = True
print(f"\n{out}")
out = (a>b) or (x<y) # False or True = True
print(f"{out}")
out = (a<b) or (x<y) # True or True = True
print(f"{out}")
out = (a>b) or (x>y) # False or False = False
print(f"{out}")
# and
out = (a<b) and (x>y) # True and False = False
print(f"\n{out}")
out = (a>b) and (x<y) # False and True = False
print(f"{out}")
out = (a<b) and (x<y) # True and True = True
print(f"{out}")
out = (a>b) and (x>y) # False and False = False
print(f"{out}")
# not
out = not(a>b)          # not(False)=True 
print(f"\n{out}")
# Membership operators
# Tuples / Collection of multi data types, enclosed in round brackets.(Immutable)
first_tuple = ("IOT", "DevOps", 47, 89, 1.5)
ans = "DevOps" in first_tuple
print(f"\n{ans}")
ans = "DevOps" not in first_tuple
print(f"{ans}")
# Identity Operators
a = 12
b = 15
result = a is b
print(f"{result}")
result = a is not b
print(f"{result}")
