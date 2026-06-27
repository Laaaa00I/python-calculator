from utils import get_number, continue_cycle
import math


while True:

    radians = get_number("Radians: ")
    degrees = radians*180/math.pi

    print(f"{radians} radians = {degrees} degrees.")

    continue_cycle()

#^^^ Main convertion cycle
