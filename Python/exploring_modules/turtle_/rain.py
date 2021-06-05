import turtle
import random
from time import sleep

wn = turtle.Screen()
wn.setup(620, 675)
wn.title('Bounce by @rmn')
wn.bgcolor('#87ceeb')
wn.tracer()

boundary = turtle.Turtle()
boundary.speed(0)
boundary.hideturtle()
boundary.width(6)
boundary.pencolor('white')
boundary.penup()
boundary.goto(300, 325)
boundary.pendown()
boundary.goto(300, -325)
boundary.goto(-300, -325)
boundary.goto(-300, 325)
boundary.goto(300, 325)

colors = ['#B7C7D5', '#CBD5E1', '#D3DDEA', '#E0E6F4',
          '#FDFDFD', '#AEBDCA', '#87bbad', '#acceba']


def single():
    wn.update()
    drop = turtle.Turtle()
    drop.hideturtle()
    drop.penup()
    drop.shape('square')
    drop.shapesize(1.2, 0.2)
    drop.color(random.choice(colors))
    drop.goto(random.randrange(-300, 300), 200)
    drop.showturtle()
    x = drop.xcor()
    drop.dy = -1

    gravity = 0.1

    while drop.ycor() > -300:
        wn.update()

        drop.sety(drop.ycor() + drop.dy)

        drop.dy -= gravity

        if drop.ycor() > 300:
            drop.dy *= -1

    drop.hideturtle()
    drop.speed(0)
    drop.pencolor('white')
    drop.pendown()
    drop.left(90)
    drop.circle(30, 120)
    drop.penup()
    drop.goto(x, -300)
    drop.pendown()
    drop.right(120)
    drop.circle(-30, 120)
    sleep(0.75)
    drop.clear()


while True:
    wn.update()
    sleep(0.1)
    single()
