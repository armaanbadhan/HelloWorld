from turtle import *

turtles()

bgcolor("#ffffff")
speed(0)
hideturtle()
pensize(5)
color("black", "grey")

penup()
goto(330, -25)   # go to back
pendown()

fillcolor()

goto(330, 75)  # back bumper
goto(150, 75)    # back trunk top
goto(150, 175)    # rear window
goto(-85, 175)     # top

right(180)
circle(20, 90, 4)

goto(-150, 75)      # front window
goto(-255, 75)    # hood

right(90)
circle(20, 90, 4)

goto(-275, -25)        # front bumper

goto(-200, -25)      # reaching tyre
right(180)
circle(-55, 180, 7)

penup()
goto(-100, -25)
pendown()

circle(-45)           # tyre 1

penup()
goto(-90, -25)
pendown()

goto(70, -25)    # between tyres

right(180)
circle(-55, 180, 7)

penup()
goto(170, -25)
pendown()

circle(-45)         # tyre 2

penup()
goto(180, -25)
pendown()

goto(330, -25)         # bottom

penup()
goto(15, 165)
pendown()

goto(-85, 165)
goto(-130, 80)
goto(15, 80)
goto(15, 165)

end_fill()

done()
