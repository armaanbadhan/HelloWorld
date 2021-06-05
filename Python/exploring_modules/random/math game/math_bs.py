from random import *


def game():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    opration = [" + ", " - ", " * "]
    y = input("what operation would you like?(+, -, *): ")

    i = 0

    if y == '+':
        i += 0
    elif y == '-':
        i += 1
    elif y == '*':
        i += 2

    x = int(input(str(num1) + opration[i] + str(num2) + " = "))

    if i == 0:
        if x == num1 + num2:
            print('great')
        else:
            print('nah')
    if i == 1:
        if x == num1 - num2:
            print('great')
        else:
            print('nah')
    if i == 2:
        if x == num1 * num2:
            print('great')
        else:
            print('nah')


game()
game()
game()
game()
