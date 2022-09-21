#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
num2 = int(num[-1])
if number > 0:
    if num2 > 5:
        print("Last digit of", number, "is", num2, "and is greater than 5")
    if num2 == 0:
        print("Last digit of", number, "is", num2, "and is 0")
    if ((num2 < 6) and (num2 != 0)):
        print("Last digit of", number, "is", num2, "and is less than 6 and not 0")
if number < 0:
    num2 = num2 * -1
    if num2 > 5:
        print("Last digit of", number, "is", num2, "and is greater than 5")
    if num2 == 0:
        print("Last digit of", number, "is", num2, "and is 0")
    if ((num2 < 6) and (num2 != 0)):
        print("Last digit of", number, "is", num2, "and is less than 6 and not 0")
