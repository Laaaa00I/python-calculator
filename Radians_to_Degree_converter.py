import math
from utils import *

while True:

    radians = get_number("Radians: ")
    degrees = radians*180/math.pi

    print(f"{radians} radians = {degrees} degrees.")

    while True:
        again = input("Would you like to continue?"
                      "\n1. Yes"
                      "\n2. No"
                      "\n").lower()
        if again in YES_ANSWERS:
            break
        elif again in NO_ANSWERS:
            print("Goodbye!")
            exit()
        else:
            print("Invalid input!")
            #^^^ This cycle stands for continuing conversions
            
#^^^ Main convertion cycle