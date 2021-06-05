from turtle import *

speed(0)
hideturtle()


def hexagon(x, y):
    fillcolor("white")
    begin_fill()
    up()
    goto(x, y)
    down()
    circle(100, 360, 6)
    up()
    left(-90)
    bk(20)
    right(-90)
    down()
    circle(80, 360, 6)
    up()
    goto(x, y)
    down()
    end_fill()


for i in range(1, 75):
    hexagon(-200 + (i * 3), 200 - (i * 3))

done()
