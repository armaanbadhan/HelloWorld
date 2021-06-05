import turtle

wn = turtle.Screen()
wn.setup(620, 675)
wn.title('Bounce by @rmn')
wn.bgcolor('#1a1a1a')

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

ball = turtle.Turtle()
ball.penup()
ball.shape('circle')
ball.color('white')

ball.dy = -2
ball.dx = 1
gravity = 0.01

while True:
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    ball.dy -= gravity

    if ball.ycor() < -300 or ball.ycor() > 300:
        ball.dy *= -1
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
