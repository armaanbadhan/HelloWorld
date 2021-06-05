"""Python program to user input pattern
using Turtle Programming
Outside_In"""
import turtle
import random

turtle.up()

x = 0
y = 0
turtle.setpos(x, y)

for x in range(8):
	turtle.color(random.random(), random.random(), random.random())
	x += 5
	y += 5
	turtle.forward(x)
	turtle.left(y)
	for _ in range(6):
		turtle.begin_fill()
		turtle.down()
		turtle.forward(40)
		turtle.left(60)
		turtle.forward(40)
		turtle.up()
		turtle.end_fill()

turtle.done()
