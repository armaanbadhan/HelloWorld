import turtle
from math import sin, cos, pi

wn = turtle.Screen()
wn.setup(height=600, width=1250)
wn.bgcolor('black')
wn.title('Projectile by @rmn')
wn.tracer(0)


def inc_angle():
    global a
    if a < 35:
        a += 0.5
    else:
        pass


def dec_angle():
    global a
    if a > -35:
        a -= 0.5
    else:
        pass


start_x, start_y = -550, -200
a = 0
arrow = turtle.Turtle()
arrow.hideturtle()
arrow.penup()
arrow.shape('arrow')
arrow.shapesize(1, 2.5)
arrow.goto(start_x, start_y)
arrow.showturtle()
arrow.color('white')
arrow.tilt(45)

ground = turtle.Turtle()
ground.hideturtle()
ground.speed(0)
ground.width(3)
ground.pencolor('white')
ground.penup()
ground.goto(-1000, start_y)
ground.pendown()
ground.goto(1000, start_y)

writeangle = turtle.Turtle()
writeangle.hideturtle()
writeangle.penup()
writeangle.color('white')
writeangle.goto(start_x + 5, start_y - 50)
writeangle.write('Angle = 45', move=False, align="center", font=("Calibri", 16, "bold"))

wn.listen()

wn.onkeypress(inc_angle, "Up")
wn.onkeypress(dec_angle, "Down")

ball = turtle.Turtle()
ball.hideturtle()
ball.penup()
ball.speed(0)
ball.shape('circle')
ball.shapesize(0.75, 0.75)
ball.color('white')
ball.goto(start_x, start_y)
ball.showturtle()
ball.pendown()

speed = 100
gravity = 10


def shoot():
    ball.penup()
    ball.goto(start_x, start_y)
    ball.pendown()
    u = speed
    acc = gravity
    angle_degree = 45 + a
    angle_pi = angle_degree * (pi/180)
    u_x = u * cos(angle_pi)
    u_y = u * sin(angle_pi)
    for i in range(10000):
        wn.update()
        t = i * 0.05
        s_x = u_x * t
        s_y = (u_y * t) - ((acc/2) * t * t)
        ball.setposition(s_x + start_x, s_y + start_y)

        if s_y < 0:
            ball.hideturtle()
            ball.penup()
            ball.goto(start_x, start_y)
            ball.showturtle()
            break


def clear():
    ball.clear()


wn.listen()
wn.onkeypress(shoot, 'z')
wn.onkeypress(clear, 'c')

while True:
    wn.update()
    arrow.tiltangle(45 + a)
    writeangle.clear()
    writeangle.write('Angle = {}'.format(45 + a), move=False, align="center", font=("Calibri", 16, "bold"))
