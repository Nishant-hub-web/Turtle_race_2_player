from turtle import Turtle

class Objects:
    def __init__(self):
        self.player_one = Turtle("turtle")
        self.player_one_init()
        self.x1 = 0
        self.x2 = 0
        self.pen=Turtle()
        self.init_pen()
        self.player_two = Turtle("turtle")
        self.player_two_init()

    def player_one_init(self):
        self.x1 = -200
        self.player_one.speed(5)
        self.player_one.color("red")
        self.player_one.penup()
        self.player_one.setx(self.x1)
        self.player_one.sety(150)

    def player_two_init(self):
        self.x2 = -200
        self.player_two.speed(5)
        self.player_two.color("green")
        self.player_two.penup()
        self.player_two.setx(self.x2)
        self.player_two.sety(-150)

    def init_pen(self):
        self.pen.speed(0)

        self.pen.penup()
        self.pen.goto(200,130)
        self.pen.pendown()
        self.pen.pen(pencolor="green",fillcolor="red",pensize=5)
        self.pen.begin_fill()
        self.pen.circle(24)
        self.pen.end_fill()
        self.pen.penup()
        self.pen.pen(pencolor="red",fillcolor="green",pensize=5)
        self.pen.goto(200, -174)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(26)
        self.pen.end_fill()
        self.pen.penup()
        self.pen.pencolor("cyan")
        self.pen.goto(-450, -250)
        self.pen.pendown()
        self.pen.goto(450,-250)
        self.pen.penup()
        self.pen.goto(0, 260)
        self.pen.write("Turtle Race!!", align="center", font=("Courier", 64, "normal"))
        self.pen.goto(-420, -300)
        self.pen.write("Player A moves:", align="left", font=("Courier", 20, "normal"))
        self.pen.goto(-420, -330)
        self.pen.pencolor("dark green")
        self.pen.write("Player B moves:", align="left", font=("Courier", 20, "normal"))
        self.pen.hideturtle()
    def player_one_move(self):
        self.player_one.pendown()
        x = self.player_one.xcor() + 10
        self.player_one.setx(x)

    def player_two_move(self):
        self.player_two.pendown()

        x = self.player_two.xcor() + 10
        self.player_two.setx(x)
