from turtle import *

hideturtle()
speed(0)

for i in range(1, 302):
    forward(10 + (i * 2))
    left(90 + (i * 0.002))

done()
