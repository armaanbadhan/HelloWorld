from math import *

x, y, z = input("Enter the coordinates :").split(",")

print("Distance = " + str(sqrt(pow(float(x), 2) + pow(float(y), 2)+pow(float(z), 2))))
