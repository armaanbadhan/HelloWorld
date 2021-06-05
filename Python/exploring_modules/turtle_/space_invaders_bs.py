import turtle

# window settings
wn = turtle.Screen()
wn.title('galaxy by armaan')
wn.bgcolor('#1a1a1a')
wn.setup(width=800, height=600)

# rocket
rocket = turtle.Turtle()
rocket.shape('triangle')
rocket.shapesize(2, 2)
rocket.color("white")
rocket.penup()
rocket.speed()
rocket.dy = 0
rocket.dx = 0
rocket.tilt(90)

points = 0

# draw boundary
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
boundary.goto(400, 240)
boundary.goto(-400, 240)


# move in directions (rocket)
def go_up():
    y = rocket.ycor()
    if y <= 190:
        y += 20
        rocket.sety(y)
    else:
        pass


def go_dn():
    y = rocket.ycor()
    if y >= -260:
        y -= 20
        rocket.sety(y)
    else:
        pass


def go_rt():
    x = rocket.xcor()
    if x <= 350:
        x += 20
        rocket.setx(x)
    else:
        pass


def go_lt():
    x = rocket.xcor()
    if x >= -350:
        x -= 20
        rocket.setx(x)
    else:
        pass


def shoot():
    bullet = turtle.Turtle()
    bullet.shape('square')
    bullet.shapesize(1, 1)
    bullet.color("white")
    bullet.penup()
    bullet.speed(1)
    bullet.dy = 0
    bullet.dx = 0
    bullet.hideturtle()
    bullet.goto(rocket.xcor(), rocket.ycor())
    bullet.left(90)
    bullet.showturtle()
    bullet.forward(450 - rocket.ycor())
    bullet.hideturtle()


# keyboard binding
wn.listen()

'''wn.onkeypress(go_up, 'w')
wn.onkeypress(go_dn, 's')
wn.onkeypress(go_rt, 'd')
wn.onkeypress(go_lt, 'a')'''

wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_dn, 'Down')
wn.onkeypress(go_rt, 'Right')
wn.onkeypress(go_lt, 'Left')
wn.onkeypress(shoot, 'z')

# to write the score
writeturtle = turtle.Turtle()
writeturtle.hideturtle()
writeturtle.penup()
writeturtle.goto(0, 245)
writeturtle.color('white')
writeturtle.write('Score = 0', move=False, align="center", font=("Calibri", 32, "bold"))


turtle.done()
