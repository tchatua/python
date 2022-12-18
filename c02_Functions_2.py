#!/usr/bin/python3
# VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstrZeneca"]
#
# keywords arguments
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

# vac_feedback("Pfizer", 95)
# vac_feedback("Unknown", 45)
vac_feedback(efficacy=34, vac="Unknown")



