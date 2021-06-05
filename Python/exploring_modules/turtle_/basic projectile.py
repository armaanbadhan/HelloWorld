import turtle
from math import cos, sin, pi

wn = turtle.Screen()
wn.tracer(1)

ball = turtle.Turtle()
ball.hideturtle()
ball.penup()
ball.setposition(-300, -200)
ball.showturtle()
ball.pendown()

u = 85
a_degree = 60

ux = u * cos(a_degree * (pi/180))
uy = u * sin(a_degree * (pi/180))

gravity = 10
ball.dy = 0

for i in range(1000):
    wn.update()
    t = i * 0.05
    sx = (ux * t)
    sy = (uy * t) - ((gravity/2) * t * t)
    ball.setposition(sx - 300, sy - 200)
    if sy < 0:
        break

turtle.done()
