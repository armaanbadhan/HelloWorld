import turtle
from time import sleep

x = turtle.Turtle()
x.hideturtle()
x.getscreen().tracer(0)

time = 5

while time >= 0:
    x.getscreen().update()
    x.clear()
    x.write('{}'.format(time), move=False, align='center', font=("Calibri", 64, "bold"))
    sleep(1)
    time -= 1
