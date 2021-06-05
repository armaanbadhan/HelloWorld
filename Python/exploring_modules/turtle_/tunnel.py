from turtle import *

hideturtle()
speed(0)
bgcolor("black")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
pencolor('black')


def triangle(q, w):
    fillcolor('red')
    begin_fill()
    up()
    goto(q, w)
    down()
    left(90)
    forward(100)
    right(180 + 30)
    forward(57.736)
    left(60)
    forward(57.736)
    end_fill()

def hexagon(x, y):
    triangle(0 + x, 0 + y)
    triangle(0 + x, 100 + y)
    triangle(86.60254037844388 + x, 150 + y)
    triangle(173.2050807568877 + x, 100 + y)
    triangle(173.2050807568876 + x, 0 + y)
    triangle(86.60254037844368 + x, -50 + y)


for i in range(1, 50):
    hexagon(-200 + (i * 10), +200 - (i * 10))

done()
