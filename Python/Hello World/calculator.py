from math import *

num1 = input("Enter a number : ")
num2 = input("Enter another number : ")
# these are strings..we need numbers...so we use int function...
# int functions makes integers so cant add decimals...so we use float

add = float(num1) + float(num2)
subtract = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)
power = pow(float(num1), float(num2))
maximum = max(num1, num2)
asd = min(num1, num2)

do = input(add)
print(do)