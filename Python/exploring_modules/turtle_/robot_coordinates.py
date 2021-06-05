import turtle

x = turtle.Turtle()

turtle.bgcolor("#b1edc3")
x.speed(0)
x.hideturtle()
x.pensize(5)
x.color("black", "grey")

'''set coordinate'''
x.penup()
x.goto(50, 120)
x.pendown()

'''eye 1'''
x.begin_fill()
x.fd(100)
x.right(90)
x.bk(100)
x.right(90)
x.fd(100)
x.right(90)
x.bk(100)
x.end_fill()

'''reach eye 2'''
x.penup()
x.goto(-50, 120)
x.pendown()

'''eye 2'''
x.begin_fill()
x.fd(100)
x.right(90)
x.bk(100)
x.right(90)
x.fd(100)
x.right(90)
x.bk(100)
x.end_fill()

'''reach nose'''
x.penup()
x.goto(0, 100)
x.pendown()

'''nose'''
x.begin_fill()
x.circle(35)
x.end_fill()

'''reach mouth'''
x.penup()
x.goto(100, 0)
x.pendown()

'''mouth'''
x.begin_fill()
x.fd(200)
x.right(90)
x.bk(90)
x.right(90)
x.fd(200)
x.right(90)
x.bk(90)
x.end_fill()

'''reach face'''
x.penup()
x.goto(100, -150)
x.pendown()

'''face'''
x.right(90)
x.forward(275)
x.right(90)
x.forward(400)
x.right(90)
x.fd(350)
x.right(90)
x.fd(400)
x.right(90)
x.fd(100)

turtle.done()
