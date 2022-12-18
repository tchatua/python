#!/usr/bin/python3
import random
# Variable Length Arguments **kwargs (keyword Arguments)
def time_activity(*args, **kwargs):
    '''
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minute + random minute spect on a random activity
    '''
    # print(f"\n{args}")
    # print(kwargs)
    min = sum(args) + random.randint(0, 60)
    # print(min)
    choice = random.choice(list(kwargs.keys()))
    # print(choice)
    print(f"\nYou have to spend {min} for {kwargs[choice]}")

time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")
