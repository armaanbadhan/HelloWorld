import turtle

wn = turtle.Screen()
wn.setup(1.0, 1.0)
wn.title('Dino by @rmn')
wn.tracer()

ground = turtle.Turtle()
ground.hideturtle()
ground.width(2)
ground.speed(0)
ground.penup()
ground.goto(-450, -150)
ground.pendown()
ground.goto(450, -150)

dino = turtle.Turtle()
dino.hideturtle()
dino.penup()
dino.shape('square')
dino.shapesize(2, 1)
dino.speed(0)
dino.goto(-350, -130)
dino.showturtle()


def jump():
    for i in range(1000):
        wn.update()
        t = i * 0.05
        s_y = (175 * t) - (90 * t * t)
        dino.sety(s_y - 128)
        if s_y < 0:
            break


def down():
    dino.goto(-350, -140)
    dino.shapesize(1, 2)


def normal():
    dino.goto(-350, -130)
    dino.shapesize(2, 1)


wn.listen()
wn.onkeypress(jump, "w")
wn.onkeypress(down, "s")
wn.onkeyrelease(normal, "s")
turtle.done()
