#!/usr/bin/python3
# Defining Function
"""
def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(2, 3)
print(f"\n{out}")
print(f"{add(10, 30)}")
#
def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)

adder(10, 50)
print(adder(10, 50))
"""
#
def summ(arg):
    x = 0
    for i in arg:
        x = x + i 
    return x 

# out = summ([1, 2, 3])
# print(f"\n{out}")
# out = summ([10, 20, 30])
# print(out)
#### Default argument
def greetings(MSG="Morning"): 
    print(f"\nGood {MSG}")
    print(f"Welcome to the function")

greetings("Morning")
greetings()
greetings("Evening")


