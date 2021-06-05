import turtle

wn = turtle.Screen()
wn.bgcolor("light grey")
wn.tracer(0)


class TrafficLight:
    def __init__(self):

        # outer box
        self.box = turtle.Turtle()
        self.box.hideturtle()
        self.box.speed(0)
        self.box.width(5)
        self.box.pencolor("black")

        # outer box draw
        self.box.penup()
        self.box.goto(-75, 200)    # top left
        self.box.pendown()
        self.box.goto(-75, -200)   # bottom left
        self.box.goto(75, -200)    # bottom right
        self.box.goto(75, 200)     # top right
        self.box.goto(-75, 200)    # top left

        """
        circle coordinates:
        (-50, 125)
        (-50, 0)
        (-50, -125)
        
        circle radius = 50
        """

        self.green_circle = turtle.Turtle()
        self.green_circle.hideturtle()
        self.green_circle.speed(0)
        self.green_circle.penup()
        self.green_circle.goto(-50, 125)
        self.green_circle.pendown()
        self.green_circle.right(90)

        self.yellow_circle = turtle.Turtle()
        self.yellow_circle.hideturtle()
        self.yellow_circle.speed(0)
        self.yellow_circle.penup()
        self.yellow_circle.goto(-50, 0)
        self.yellow_circle.pendown()
        self.yellow_circle.right(90)

        self.red_circle = turtle.Turtle()
        self.red_circle.hideturtle()
        self.red_circle.speed(0)
        self.red_circle.penup()
        self.red_circle.goto(-50, -125)
        self.red_circle.pendown()
        self.red_circle.right(90)

        def color():
            if color == 'red':
                self.green_circle.begin_fill()
                self.green_circle.circle(50)
                self.green_circle.color('grey')
                self.green_circle.end_fill()

                self.yellow_circle.begin_fill()
                self.yellow_circle.circle(50)
                self.yellow_circle.color('grey')
                self.yellow_circle.end_fill()

                self.red_circle.begin_fill()
                self.red_circle.circle(50)
                self.red_circle.color('grey')
                self.red_circle.end_fill()

        wn.update()


traffic1 = TrafficLight

turtle.done()
