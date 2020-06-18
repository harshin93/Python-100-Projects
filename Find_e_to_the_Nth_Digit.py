# Find e to the Nth Digit - Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

import math
e_value = math.e

x = int(input("Enter your Rounding digit: "))
while x <= 15:
    print (round(e_value,x))
    break
else:
    print("Not a Valid Input")
