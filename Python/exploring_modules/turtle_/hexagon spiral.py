from turtle import *

bgcolor("black")
speed(0)
hideturtle()

i = 0
times = 145

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

while i != times:
    width(int(round(i/100 + 1, 0)))
    pencolor(colors[(i % 6) - 1])
    fd(1 + (i * 1))
    right(-60 + (i * 0.01))
    i += 1

done()
