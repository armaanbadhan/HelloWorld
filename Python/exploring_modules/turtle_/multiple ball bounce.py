import turtle
import random

wn = turtle.Screen()
wn.setup(620, 675)
wn.title('Bounce by @rmn')
wn.bgcolor('#1a1a1a')
wn.tracer(0)

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

shapes = ['square', 'circle', 'triangle']
colors = ['red', 'orange', 'yellow', 'green', 'blue']

balls = []

for i in range(20):
    balls.append(turtle.Turtle())

for ball in balls:
    ball.penup()
    ball.speed(0)
    ball.hideturtle()
    ball.goto(random.randrange(-290, 290), random.randrange(150, 290))
    ball.showturtle()
    ball.shape(random.choice(shapes))
    ball.color(random.random(), random.random(), random.random())
    ball.dy = 0
    ball.dx = random.randrange(-3, 3)
    ball.da = random.randrange(-5, 5)

gravity = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # wall collision
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1
        if ball.ycor() > 300:
            ball.dy *= -1
            ball.da *= -1
        if ball.xcor() > 290 or ball.xcor() < -290:
            ball.dx *= -1
            ball.da *= -1
