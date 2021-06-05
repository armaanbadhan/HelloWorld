import turtle
import time

wn = turtle.Screen()
wn.bgcolor("light grey")
wn.tracer(0)

# outer box
box = turtle.Turtle()
box.hideturtle()
box.speed(0)
box.width(5)
box.pencolor("black")
# outer box draw
box.penup()
box.goto(-75, 200)    # top left
box.pendown()
box.goto(-75, -200)   # bottom left
box.goto(75, -200)    # bottom right
box.goto(75, 200)     # top right
box.goto(-75, 200)    # top left


"""
circle coordinates:
(-50, 125)
(-50, 0)
(-50, -125)

circle radius = 50
"""

green_circle = turtle.Turtle()
green_circle.hideturtle()
green_circle.speed(0)
green_circle.penup()
green_circle.goto(-50, 125)
green_circle.pendown()
green_circle.right(90)

yellow_circle = turtle.Turtle()
yellow_circle.hideturtle()
yellow_circle.speed(0)
yellow_circle.penup()
yellow_circle.goto(-50, 0)
yellow_circle.pendown()
yellow_circle.right(90)

red_circle = turtle.Turtle()
red_circle.hideturtle()
red_circle.speed(0)
red_circle.penup()
red_circle.goto(-50, -125)
red_circle.pendown()
red_circle.right(90)

greencolor = "grey"
yellowcolor = "grey"
redcolor = "red"

greentime = 0.1
yellowtime = 0.1
redtime = 0.1

start_time = time.time()

while True:
    wn.update()

    green_circle.begin_fill()
    green_circle.circle(50)
    green_circle.color(greencolor)
    green_circle.end_fill()

    yellow_circle.begin_fill()
    yellow_circle.circle(50)
    yellow_circle.color(yellowcolor)
    yellow_circle.end_fill()

    red_circle.begin_fill()
    red_circle.circle(50)
    red_circle.color(redcolor)
    red_circle.end_fill()

    if time.time() > start_time + redtime:
        greencolor = "green"
        yellowcolor = "grey"
        redcolor = "grey"

        if time.time() > start_time + redtime + greentime:
            greencolor = "grey"
            yellowcolor = "yellow"
            redcolor = "grey"

            if time.time() > start_time + redtime + greentime + yellowtime:
                greencolor = "grey"
                yellowcolor = "grey"
                redcolor = "red"
                start_time = time.time()
