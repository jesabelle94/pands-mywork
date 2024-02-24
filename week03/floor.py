# floor.py - floors a number
# Author: Jenny Formentera
# Take a float number and output an int rounded down number
# math module - math.floor()
# Enter a float number: -5.99
# 5.99 floored is 6

import math

numberTofloor = float(input("Enter a number:"))
flooredNumber = math.floor(numberTofloor)
print(' {} floored is {}' .format(numberTofloor, flooredNumber))