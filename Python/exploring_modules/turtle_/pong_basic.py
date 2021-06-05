import turtle
import random

# window setting
wn = turtle.Screen()
wn.bgcolor('#1a1a1a')
wn.title("PONG by Armaan")
wn.setup(width=800, height=600)
wn.tracer()

# board 1
player1 = turtle.Turtle()
player1.hideturtle()
player1.speed(0)
player1.shape('square')
player1.shapesize(5, 1)
player1.color("white")
player1.penup()
player1.goto(-375, 0)
player1.showturtle()

# board 2
player2 = turtle.Turtle()
player2.hideturtle()
player2.speed(0)
player2.shape('square')
player2.shapesize(5, 1)
player2.color("white")
player2.penup()
player2.goto(375, 0)
player2.showturtle()

# ball
go_x = [random.randrange(-3, -1), random.randrange(1, 3)]
cango_x = go_x[random.randint(0, 1)]
go_y = [random.randrange(-3, -1), random.randrange(1, 3)]
cango_y = go_y[random.randint(0, 1)]

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = cango_x
ball.dy = cango_y

# points
points_p1 = 0
points_p2 = 0


# functions for moving
def go_up_1():        # player 1 up
    y = player1.ycor()
    if y <= 225:
        y += 25
        player1.setposition(-375, y)


def go_dn_1():        # player 1 down
    y = player1.ycor()
    if y >= -225:
        y -= 25
        player1.setposition(-375, y)


def go_up_2():          # player 2 up
    y = player2.ycor()
    if y <= 225:
        y += 25
        player2.setposition(375, y)


def go_dn_2():          # player 2 down
    y = player2.ycor()
    if y >= -225:
        y -= 25
        player2.setposition(375, y)


# move boards
wn.listen()
wn.onkeypress(go_up_1, "w")
wn.onkeypress(go_dn_1, "s")
wn.onkeypress(go_up_2, "o")
wn.onkeypress(go_dn_2, "l")

# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >= 390:
        go_x = [random.randrange(-3, -1), random.randrange(1, 3)]
        cango_x = go_x[random.randint(0, 1)]
        go_y = [random.randrange(-3, -1), random.randrange(1, 3)]
        cango_y = go_y[random.randint(0, 1)]
        ball.dx = cango_x
        ball.dy = cango_y
        ball.goto(0, 0)
        ball.dx *= -1
        points_p1 += 1

    if ball.xcor() <= -390:
        go_x = [random.randrange(-3, -1), random.randrange(1, 3)]
        cango_x = go_x[random.randint(0, 1)]
        go_y = [random.randrange(-3, -1), random.randrange(1, 3)]
        cango_y = go_y[random.randint(0, 1)]
        ball.dx = cango_x
        ball.dy = cango_y
        ball.goto(0, 0)
        ball.dx *= -1
        points_p2 += 1
        
    # paddle ball collison
    if player1.ycor() - 50 <= ball.ycor() <= player1.ycor() + 50 and ball.xcor() <= -375:
        ball.dx *= -1
    if player2.ycor() - 50 <= ball.ycor() <= player2.ycor() + 50 and ball.xcor() >= 375:
        ball.dx *= -1
