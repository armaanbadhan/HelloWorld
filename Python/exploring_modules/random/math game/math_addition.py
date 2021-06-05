from random import *
import time

points = 0
played = 0
times = 5
timeout = 50
print('welcome to addition game you have 5 chances')

start_time = time.time()

while played != times and time.time() < start_time + timeout:
    num1 = randint(100, 999)
    num2 = randint(100, 999)
    ans = int(input(str(num1) + " + " + str(num2) + " = "))
    if ans == num1 + num2:
        points += 1
    played += 1

elapsed_time = time.time() - start_time

time_taken = round(elapsed_time, 2)
print("You scored " + str(points) + ' / ' + str(played) + " points.")
print('You took ' + str(time_taken) + ' seconds to complete.')
print("You took " + str(round(time_taken/played, 2)) + " seconds per question.")
