#!/usr/bin/python3
#
import random
#
def vac_feedback(vac, efficacy):
    print(f"\n{vac} Vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effective, Needs more trial") 
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif efficacy >= 90:
        print("Sure, will take a shot.")
    else:
        print("Needs many more trials.")
# vac_feedback(vac=34, efficacy="Unknown")
#
def order_food(min_order, *args):
    print(f"\nYou have ordered: {min_order}")
    # print(args)
    for item in args:
        print(f"You have ordered: {item}")
    print("-- Your food will be delivered in 30 mins:")
    print("Enjoy the party")
# order_food("Salad", "Pizza", "Biryani", "Soup")
#
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
# time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")
#
