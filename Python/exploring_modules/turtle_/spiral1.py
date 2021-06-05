import turtle

x = turtle.Turtle()

x.speed(0)
x.hideturtle()

colors = ["#85DB24", "#24DBD5", "#7A24DB", "#DB242A"]

for i in range(1, 60):
    # x.fillcolor(colors[(i % 4) - 1])
    # x.begin_fill()
    x.circle(5 * i)
    x.circle(-5 * i)
    x.right(i)
    # x.end_fill()

turtle.done()
