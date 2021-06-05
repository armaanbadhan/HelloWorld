import turtle

wn = turtle.Screen()
wn.title('Tic Tac Toe by @rmn')
wn.tracer(0)

lines = turtle.Turtle()
lines.hideturtle()
lines.speed(0)
lines.width(3)
lines.pencolor()
lines.penup()
lines.goto(-60, 180)
lines.pendown()
lines.goto(-60, -180)
lines.penup()
lines.goto(60, -180)
lines.pendown()
lines.goto(60, 180)
lines.penup()
lines.goto(180, 60)
lines.pendown()
lines.goto(-180, 60)
lines.penup()
lines.goto(-180, -60)
lines.pendown()
lines.goto(180, -60)

turn = 'circle'


def makecross(x, y):
    cross = turtle.Turtle()
    cross.hideturtle()
    cross.width(2)
    cross.speed(0)
    cross.penup()
    cross.goto(x * 120, y * 120)
    cross.pendown()
    cross.right(45)
    cross.forward(50)
    cross.backward(100)
    cross.forward(50)
    cross.right(90)
    cross.forward(50)
    cross.backward(100)
    cross.forward(50)
    global turn
    turn = 'circle'


def makecircle(x, y):
    circle_ = turtle.Turtle()
    circle_.hideturtle()
    circle_.width(2)
    circle_.speed(0)
    circle_.penup()
    circle_.goto((x * 120) - 50, y * 120)
    circle_.right(90)
    circle_.pendown()
    circle_.circle(50)
    global turn
    turn = 'cross'


def make(x, y):
    if turn == 'circle':
        makecircle(x, y)
    if turn == 'cross':
        makecross(x, y)


draw = ''

while True:
    wn.update()
    while True:
        try:
            draw = input('where would you like to draw: ')
            break
        except ValueError:
            print('try again')
            continue

    if draw == '1':
        x = -1
        y = 1
        make(x, y)
    elif draw == '2':
        x = 0
        y = 1
        make(x, y)
    elif draw == '3':
        x = 1
        y = 1
        make(x, y)
    elif draw == '4':
        x = -1
        y = 0
        make(x, y)
    elif draw == '5':
        x = 0
        y = 0
        make(x, y)
    elif draw == '6':
        x = 1
        y = 0
        make(x, y)
    elif draw == '7':
        x = -1
        y = -1
        make(x, y)
    elif draw == '8':
        x = 0
        y = -1
        make(x, y)
    elif draw == '9':
        x = 1
        y = -1
    else:
        continue
