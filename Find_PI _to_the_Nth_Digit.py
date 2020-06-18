Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.

import math
pi_value = math.pi

x = int(input("Enter your Rounding digit: "))
while x <= 15:
    print (round(pi_value,x))
    break
else:
    print("Not a Valid Input")
