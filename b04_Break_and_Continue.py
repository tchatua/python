#!/usr/bin/python3
"""
print("")
# Break Statement
for i in "DevOps":
    print(f"{i}")
    if i == "O":
        print("Found my data")
        break
print(f"\nOut of Loop")
#
# Continue Statement
for i in "DevOps":
    if i == "O":
        print("Found my data")
        continue
    print(f"Value of i is {i}")
print(f"\nOut of Loop")
"""
#
import random 
VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstrZeneca"]

random.shuffle(VACCINES)
print(f"\n{VACCINES}")

LUCKY = random.choice(VACCINES)
print(f"{LUCKY}")

for vac in VACCINES:
    print(f"******TESTING VACCINES {vac}.")
    if vac == LUCKY:
        print("###################################")
        print(f"{LUCKY} vaccine, Test Successful")
        print("###################################")
        break
    print("XXXXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXXXX")


