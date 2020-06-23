import math


total_amount = float(input("Enter your total purchase amount: "))
total_money = float(input("Enter your payment: "))




if total_money > total_amount:
    change = int((total_money - total_amount) * 100)
    
    print("Change is {}".format(change))
    print("Change Breakdown")

    quarters = int(change / 25)
    # change = 0
    change =change - quarters * 25
    print("Quarters {}".format(quarters))

    dime = int(change / 10)
    change -= dime * 10
    print("Dime {}".format(dime)) 

    fives = int(change / 5)
    change -= fives * 5
    print("Five {}".format(fives))

    penny = int(change / 1)
    change -= penny * 1
    print("Penny {}".format(penny))

elif total_amount == total_money:
    print("Amount Paid in full")

else:
    print("Invalid Amount")