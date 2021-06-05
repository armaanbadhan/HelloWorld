import turtle
from math import atan2, pi

wn = turtle.Screen()
wn.title('Coin Collect')
wn.bgcolor('#1a1a1a')
wn.setup(width=800, height=600)

point_to = turtle.Turtle()
point_to.shape('square')
point_to.color("grey")
point_to.penup()
point_to.speed()

pointer = turtle.Turtle()
pointer.shape('arrow')
pointer.shapesize(3, 3)

boundary = turtle.Turtle()
boundary.speed(0)
boundary.hideturtle()
boundary.width(6)
boundary.pencolor('white')
boundary.penup()
boundary.goto(400, 300)
boundary.pendown()
boundary.goto(400, -300)
boundary.goto(-400, -300)
boundary.goto(-400, 300)
boundary.goto(400, 300)


def go_up():
    y = point_to.ycor()
    if y <= 260:
        y += 20
        point_to.sety(y)
    else:
        pass


def go_dn():
    y = point_to.ycor()
    if y >= -260:
        y -= 20
        point_to.sety(y)
    else:
        pass


def go_rt():
    x = point_to.xcor()
    if x <= 360:
        x += 20
        point_to.setx(x)
    else:
        pass


def go_lt():
    x = point_to.xcor()
    if x >= -360:
        x -= 20
        point_to.setx(x)
    else:
        pass


wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_dn, 'Down')
wn.onkeypress(go_rt, 'Right')
wn.onkeypress(go_lt, 'Left')

while True:
    wn.update()
    x_ = point_to.xcor()
    y_ = point_to.ycor()
    ang_rad = atan2(y_, x_)
    ang_deg = ang_rad * (180/pi)
    pointer.settiltangle(ang_deg)
