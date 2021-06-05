import turtle

y = turtle.Turtle()
y.speed(0)
y.hideturtle()
y.getscreen().bgcolor("#ffffff")

for i in range(5):
    y.left(144)
    y.bk(500)
    for j in range(5):
        y.left(144)
        y.bk(125)
        for k in range(5):
            y.left(144)
            y.bk(30)
            for q in range(5):
                y.left(144)
                y.bk(8)


turtle.done()
