import turtle

x = turtle.Turtle()

'''
x.color('blue', 'cyan')

x.begin_fill()

# ISOCELES TRAANGLE
x.fd(100)
x.right(75)
x.bk(200)
x.right(30)
x.fd(200)

x.end_fill()
'''

'''
EQUILATERAL TRIANGLE
x.speed(1)
x.fd(100)
x.right(60)
x.bk(100)
x.right(60)
x.fd(100)
'''

# robo face

turtle.bgcolor("#b1edc3")
x.speed(0)
x.hideturtle()
x.pensize(5)
x.color("black", "grey")

'''set coordinate'''
x.penup()
x.forward(50)
x.left(90)
x.forward(120)
x.right(90)
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
x.left(90)
x.forward(200)
x.left(180)
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
x.right(90)
x.fd(150)
x.left(90)
x.bk(20)
x.right(270)
x.pendown()

'''nose'''
x.begin_fill()
x.circle(35)
x.end_fill()

'''reach mouth'''
x.penup()
x.left(90)
x.fd(95)
x.left(90)
x.forward(100)
x.right(180)
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
x.forward(140)
x.right(90)
x.pendown()

'''face'''
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
