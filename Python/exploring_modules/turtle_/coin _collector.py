import turtle
import random
import time

wn = turtle.Screen()
wn.title('Coin Collect')
wn.bgcolor('#1a1a1a')
wn.setup(width=800, height=600)

collector = turtle.Turtle()
collector.shape('square')
collector.color("grey")
collector.penup()
collector.speed()

points = 0

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
    y = collector.ycor()
    if y <= 260:
        y += 20
        collector.sety(y)
    else:
        pass


def go_dn():
    y = collector.ycor()
    if y >= -260:
        y -= 20
        collector.sety(y)
    else:
        pass


def go_rt():
    x = collector.xcor()
    if x <= 360:
        x += 20
        collector.setx(x)
    else:
        pass


def go_lt():
    x = collector.xcor()
    if x >= -360:
        x -= 20
        collector.setx(x)
    else:
        pass


wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_dn, 's')
wn.onkeypress(go_rt, 'd')
wn.onkeypress(go_lt, 'a')

coin = turtle.Turtle()
coin.shape('circle')
coin.color("yellow")
coin.penup()
coin.speed()
coin.hideturtle()
coin.setposition(random.randint(-18, 18) * 20, random.randint(-13, 13) * 20)
coin.showturtle()

start_time = time.time()
timeout = 1 * 60

while time.time() < start_time + timeout and points != 15:
    wn.update()

    if coin.xcor() == collector.xcor() and coin.ycor() == collector.ycor():
        points += 1
        coin.hideturtle()
        coin.setposition(random.randint(-18, 18) * 20, random.randint(-13, 13) * 20)
        coin.showturtle()

if points != 15:
    print('You scored ' + str(points) + ' points in 1 minute.')
elif time.time() < start_time + timeout:
    elapsed_time = time.time() - start_time
    print("Great! You took " + str(round(elapsed_time, 2)) + " seconds")
