from turtle import *

speed(0)
hideturtle()
pensize(3)


def tyre(x, y):
    up()
    goto(x, y)
    down()
    fillcolor("#333333")
    begin_fill()
    circle(48)
    end_fill()


up()
goto(-500, -200)
down()
goto(500, -200)

tyre(-218, -200)
tyre(218, -200)

up()                  # base
goto(-150, -150)
down()
goto(147, -150)

right(270)
circle(-70, 180, 3)

right(265)
forward(75)

left(70)      # back
fd(115)
goto(-300, -60)
goto(-290, -150)

right(-15)
circle(-70, 180, 3)

up()
goto(-300, -60)
down()

goto(-20, 60)          # reach tip
goto(390, -30)      # reach tail

up()
goto(-20, 40)      # window tip
down()

goto(270, -20)

goto(-200, -35)
goto(-20, 40)
goto(-15, -30)

done()
