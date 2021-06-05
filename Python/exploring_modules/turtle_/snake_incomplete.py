import turtle
import random

wn = turtle.Screen()
wn.title('Snake by ARMAAN')
wn.bgcolor('#1a1a1a')
wn.setup(width=800, height=600)

snake_head = turtle.Turtle()
snake_head.shape('square')
snake_head.color("grey")
snake_head.penup()
snake_head.speed()
snake_head.dy = 0
snake_head.dx = 0
snake_head.direction = 'stop'
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
boundary.goto(400, 240)
boundary.goto(-400, 240)


def go_up():
    y = snake_head.ycor()
    if y <= 200 and snake_head.direction != "down":
        y += 20
        snake_head.sety(y)
    else:
        pass


def go_dn():
    y = snake_head.ycor()
    if y >= -260:
        y -= 20
        snake_head.sety(y)
    else:
        pass


def go_rt():
    x = snake_head.xcor()
    if x <= 360:
        x += 20
        snake_head.setx(x)
    else:
        pass


def go_lt():
    x = snake_head.xcor()
    if x >= -360:
        x -= 20
        snake_head.setx(x)
    else:
        pass


def move():
    if snake_head.direction == "up":
        snake_head.sety(snake_head.ycor() + 20)
    if snake_head.direction == "down":
        snake_head.sety(snake_head.ycor() - 20)
    if snake_head.direction == "right":
        snake_head.setx(snake_head.xcor() + 20)
    if snake_head.direction == "left":
        snake_head.setx(snake_head.xcor() - 20)


wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_dn, 's')
wn.onkeypress(go_rt, 'd')
wn.onkeypress(go_lt, 'a')
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_dn, 'Down')
wn.onkeypress(go_rt, 'Right')
wn.onkeypress(go_lt, 'Left')

food = turtle.Turtle()
food.shape('circle')
food.color("yellow")
food.penup()
food.speed()
food.hideturtle()
food.setposition(random.randint(-18, 18) * 20, random.randint(-13, 10) * 20)
food.showturtle()

writeturtle = turtle.Turtle()
writeturtle.hideturtle()
writeturtle.penup()
writeturtle.goto(0, 245)
writeturtle.color('white')
writeturtle.write('Score = 0', move=False, align="center", font=("Calibri", 32, "bold"))

while True:
    wn.update()
    # move()

    # if snake eats food
    if food.xcor() == snake_head.xcor() and food.ycor() == snake_head.ycor():
        points += 1
        food.hideturtle()
        food.setposition(random.randint(-18, 18) * 20, random.randint(-13, 10) * 20)
        food.showturtle()
        writeturtle.clear()
        writeturtle.write('Score = {}'.format(points),
                          move=False, align="center", font=("Calibri", 32, "bold"))
